#!/usr/bin/python3
# 5-to_json_string.py
# Author: Hanif miyanji
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
