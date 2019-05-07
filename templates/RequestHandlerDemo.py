# -*- coding: utf-8 -*-
import json, requests


class RequestHandler():


    def __init__(self):
        pass


    def get_reply(self, sentence):
        # TODO Write your own method here.
        result = sentence.replace(u'你', u'我').replace(u'？', u'。')
        return result


    def get_batch_replies(self, question_set):
        result_set = []
        for question in question_set:
            result = {'qid': question['qid'], 'result': ''}
            try:
                result['result'] = self.get_reply(question['question'])
            except Exception as e:
                print e
            result_set.append(result)
        return result_set

