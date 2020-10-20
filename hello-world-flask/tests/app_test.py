#!/usr/bin/env python

from helloworld import app

import os
import json
import unittest


class AppTest(unittest.TestCase):
  def setUp(self):
    self.app = app.app.test_client()

  def tearDown(self):
    del self.app

  def test_app(self):
    response = self.app.get('/', content_type='application/json')

    expected_env_vars = [
      'PATH',
      'HOSTNAME',
      'HOME',
      'LANG'
    ]

    expected_yaml = {
      'version': 'v1',
      'build': 'foo',
      'container_sha': 'bar'
    }

    response_data = json.loads(response.get_data(as_text=True))
    self.assertEquals(response.status_code, 200)

    self.assertDictContainsKey(response_data, 'env')
    self.assertDictContainsKey(response_data, 'yaml')
    self.assertEquals(response_data['yaml'], expected_yaml)

    for var in expected_env_vars:
      self.assertDictContainsKey(response_data['env'], var)
      self.assertEquals(response_data['env'][var], os.environ[var])

  def test_wordcount(self):
    post_data = {
      'input_string': 'The quick brown fox jumps over the lazy dog.'
    }

    expected_output = {
        "input": "The quick brown fox jumps over the lazy dog.",
        "occurrances": {
          "the": 2,
          "quick": 1,
          "brown": 1,
          "fox": 1,
          "jumps": 1,
          "over": 1,
          "lazy": 1,
          "dog": 1
        },
        "total": 9,
        "most_common": 'the'
    }

    response = self.app.post('/wordcount',
                              data=json.dumps(post_data),
                              content_type='application/json')

    response_json = json.loads(response.get_data(as_text=True))

    self.assertEquals(response.status_code, 200)

    self.assertEqual(response_json, expected_output)

  def assertDictContainsKey(self, dictionary, key):
    self.assertIsNotNone(dictionary.get(key))

if __name__ == '__main__':
  unittest.main()
