from collections import namedtuple
import ujson as json



def serializable_namedtuple(*args, **kwargs):
  """
  A json serializable object with fields _fields
  """
  cls = namedtuple(*args, **kwargs)

  def dumps(self):
    return json.dumps({f: self.__getattribute__(f) for f in self._fields})
  setattr(cls, 'dumps', dumps)

  def loads(cls, string):
    js = json.loads(string)
    return cls(**{k: js[k] for k in cls._fields})
  setattr(cls, 'loads', classmethod(loads))

  return cls

# Student submission
SerializedSubmission = serializable_namedtuple('Submission', [
  'question_name',  # a stirng specifying the question name
  'submission'      # a possibly blank string.
])

SerializedScore = serializable_namedtuple('Score', [
  'score',      # a number between 0.1 and 1.0
  'error_msg'   # a possibly blank string.
])

SerializedQuestion = serializable_namedtuple('Question', [
  'name',         # a string unique identifier for the question
  'scorer_name',  # the name of hte scorer to use
  'scorer_params', # a json object passed to the scorer object (see scorer)
  'test_cases'
])
