#!/usr/bin/env python

from collections import Counter
from string import punctuation

import os
import yaml

def get_all_env_vars():
  return dict(os.environ)

def get_yaml_data():
  pwd = os.path.dirname(os.path.realpath(__file__))
  data_file = os.path.join(pwd, 'data.yaml')
  file_stream = open(data_file, 'r')
  return yaml.load(file_stream)

def get_word_count(input_string):
  punctuation_set = set(punctuation)

  def remove_punctuation(word):
    return ''.join((letter.lower()
                    for letter in word
                    if letter not in punctuation_set))

  return Counter((remove_punctuation(word)
                  for word in input_string.split(' ')))
