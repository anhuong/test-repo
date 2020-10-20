#!/usr/bin/env python

from helloworld import utils

import os
import unittest


class UtilsTest(unittest.TestCase):
  def test_get_yaml_data(self):
    yaml_data = utils.get_yaml_data()
    self.assertEquals(yaml_data['version'], 'v1')
    self.assertEquals(yaml_data['build'], 'foo')
    self.assertEquals(yaml_data['container_sha'], 'bar')

  def test_get_all_env_vars(self):
    self.assertEquals(utils.get_all_env_vars(),
                      dict(os.environ))

  def test_word_count(self):
    input_data = 'The quick brown fox jumps over the lazy dog.'
    expected_result = {
        "the": 2,
        "quick": 1,
        "brown": 1,
        "fox": 1,
        "jumps": 1,
        "over": 1,
        "lazy": 1,
        "dog": 1
    }

    result = utils.get_word_count(input_data)
    self.assertEquals(result, expected_result)

if __name__ == '__main__':
  unittest.main()
