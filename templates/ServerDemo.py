# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, request
from RequestHandlerDemo import RequestHandler


app = Flask(__name__)
Handler = RequestHandler()


@app.route('/nlpcc_2019', methods=['POST'])
def single_round():
    question_set = request.json.get('questionSet')
    result_set = Handler.get_batch_replies(question_set)
    return jsonify({'resultSet': result_set})


@app.route('/nlpcc_2019/multiround', methods=['GET'])
def multi_round():
    question = request.values.get('question')
    session_id = request.values.get('sessionId')
    reply = Handler.get_reply(question)
    return jsonify({'answer': reply, 'sessionId': session_id, 'question': question})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2019)
