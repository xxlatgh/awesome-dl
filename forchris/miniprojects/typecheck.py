#!/usr/bin/env python
from __future__ import print_function

import sys
import json
import pyparsing as pp
import jsonschema
import numpy as np

length = pp.Word(pp.nums).setParseAction(lambda tokens: int(tokens[0]))

def array_validator(tokens):
    length, subschema = tokens
    return {"type": "array", "minItems": length, "maxItems": length,
            "items": subschema}

def tuple_validator(tokens):
    length = len(tokens)
    return {"type": "array",
            "items": tokens.asList(),
            "minItems": length,     # prevent missing items
            "maxItems": length}     # prevent extra items

def generate_expr():
    number = pp.Literal("number").setParseAction(lambda: {"type": "number"})
    string = pp.Literal("string").setParseAction(lambda: {"type": "string"})
    count = pp.Literal("count") \
              .setParseAction(lambda: {"type": "integer", "minimum": 0})

    expr = pp.Forward()
    tuple = (pp.Suppress(pp.Literal("(")) +
             pp.delimitedList(expr) +
             pp.Suppress(pp.Literal(")"))).setParseAction(tuple_validator)

    array = (length + pp.Suppress("*") + expr).setParseAction(array_validator)
    expr << (tuple | number | string | count | array)

    return pp.LineStart() + expr + pp.LineEnd()     # throw error on extra stuff

expr = generate_expr()

def dshape_to_schema(dshape):
    # this is janky, fix
    if dshape.startswith('{'):
        schema_dict = json.loads(dshape)
        props_vals = {key: dshape_to_schema(val) for key, val in schema_dict.iteritems()}
        schema = {"type": "object", "properties": props_vals,
                  "required": props_vals.keys(), "additionalProperties": False}

        return schema

    try:
        return expr.parseString(dshape)[0]
    except pp.ParseException as e:
        print("Bad dshape {}".format(dshape))
        raise e

def get_validator(type_str):
    schema = dshape_to_schema(type_str)
    types = {"array": (tuple, list, np.ndarray)}
    return jsonschema.Draft4Validator(schema, types=types)
