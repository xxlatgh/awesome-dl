from collections import namedtuple
from functools import wraps
from importlib import import_module
import json
import os
import requests
import sys
import jsonschema

from serializers import SerializedSubmission, SerializedScore, SerializedQuestion
from typecheck import get_validator

BASE_URL = "https://www.thedataincubator.com"

try:
  # ~/.ssh is safe, hopefully
  with open('/home/vagrant/.ssh/.grader_secret') as secret_f:
    SECRET_GRADER_KEY = secret_f.read().strip()
except IOError: # for local dev / general issues
  print "WARNING: You are missing a unique key. Scores will still be reported, but not scored."
  print "Please show this message to a TDI staff member."
  SECRET_GRADER_KEY = 'bcgzmGuIB9yAlmshSuLy'

def is_invalid(answer, type_str):
  try:
    get_validator(type_str).validate(answer)
  except jsonschema.ValidationError as e:
    return e

  return None


def test_cases_grading(question_name, func, test_cases):
  res = []
  for test_case in test_cases:
    #test func with params in
    sub_res = func(*test_case['args'], **test_case['kwargs'])
    invalid = is_invalid(sub_res, test_case['type_str'])
    if invalid:
      print(invalid)
      return
    res.append(sub_res)

  # Submission

  submission = SerializedSubmission(question_name=question_name, submission=res)
  r = requests.post(BASE_URL + '/submission?api_key=%s' % SECRET_GRADER_KEY,
                 data={'submission': submission.dumps()})
  print "=================="
  if r.status_code != 200:
    print "Something went wrong"
    return
  score = SerializedScore.loads(r.text)

  if score.error_msg:
    print "Error: ", score.error_msg
  else:
    print "Your score: ", score.score
  print "=================="


def score(question_name, func):
  # Get test cases
  resp = requests.get(BASE_URL + '/test_cases/%s?api_key=%s' % (question_name, SECRET_GRADER_KEY))
  if resp.status_code != 200:
    print "No question found:", question_name
    return
  test_cases = json.loads(resp.text)
  test_cases_grading(question_name, func, test_cases)

# for local dev
def local_score(question_name, func):
  """
  Score locally in developer mode
  """
  # call this here because students don't have scorers
  import scorers
  import inspect
  reload(scorers)
  scorers_by_name = dict(inspect.getmembers(scorers))

  all_questions = {}
  for miniproject in scorers.get_miniprojects():
    module = import_module(miniproject)
    reload(module)
    for question in module.questions:
      all_questions[question['name']] = question

  q = all_questions[question_name]
  test_cases = q['test_cases']
  for test_case in test_cases:
    result = func(*test_case['args'], **test_case['kwargs'])
    invalid = is_invalid(result, test_case['type_str'])
    if invalid:
      print(invalid)
      return

    answer = test_case['answer']
    Scorer = scorers_by_name[q['scorer_name']](**q['scorer_params'])
    return Scorer.score(result, answer)

client_mode = os.environ.get("GRADER_CLIENT_MODE", None)
if client_mode == "local":
  score = local_score
elif client_mode == "local_gae":
  BASE_URL = "http://localhost:8080"
