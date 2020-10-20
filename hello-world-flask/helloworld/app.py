#/usr/bin/env python

from flask import Flask, jsonify, request
from helloworld import utils

app = Flask(__name__)

@app.route('/')
def main():
  data_to_return = {
    'env': utils.get_all_env_vars(),
    'yaml': utils.get_yaml_data(),
    "hello": "world"
  }

  return jsonify(data_to_return)

@app.route('/wordcount', methods=['POST'])
def word_count():
  request_arguments = request.get_json()
  input_string = request_arguments.get('input_string')

  word_count = utils.get_word_count(input_string)

  return jsonify({
      "input": input_string,
      "occurrances": word_count,
      "total": sum(word_count.values()),
      "most_common": word_count.most_common(1)[0][0]
  })
