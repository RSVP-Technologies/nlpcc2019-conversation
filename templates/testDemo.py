# -*- coding: utf-8 -*-
import json, requests, time


def test_single_round_batch():
    url = "http://0.0.0.0:2019/nlpcc_2019"
    question_set = [
        {'qid': 1, 'question': '你好'},
        {'qid': 2, 'question': '你叫什么名字'},
        {'qid': 3, 'question': '明天天气怎么样'}
    ]
    questions = {'questionSet': question_set}
    headers = {'Content-type': 'application/json'}
    try:
        r = requests.post(url, data = json.dumps(questions), headers = headers, timeout = 3)
        if r.status_code == 200:
            data = r.json()
            print(json.dumps(data, ensure_ascii=False))
            result_set = data['resultSet']
            for result in result_set:
                print(str(result['qid']) + ': ' + result['result'])
        else:
            print("status_code error: " + str(r.status_code))
    except Exception as e:
        print e


def test_multi_round():
    url = 'http://0.0.0.0:2019/nlpcc_2019/multiround'
    session_id = "123456"
    sentence = '你叫什么？'
    headers = {'Content-type': 'application/json'}
    try:
        r = requests.get(url, params = {'question': sentence, 'sessionId': session_id}, headers = headers, timeout = 5)
        if r.status_code == 200:
            data = r.json()
            print(json.dumps(data, ensure_ascii=False))
        else:
            print("status_code error: " + str(r.status_code))
    except Exception as e:
        print e


if __name__ == '__main__':
    test_single_round_batch()
    test_multi_round()

