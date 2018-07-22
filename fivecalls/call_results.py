from datetime import datetime
from pathlib import Path

import requests
from yaml import load, dump
from yaml.parser import ParserError

from fivecalls.singleton import Singleton


class CallResults(metaclass=Singleton):

    def __init__(self):
        self.db_path = 'data/results.yaml'
        self.new_results = False

        if not Path(self.db_path).exists():
            self.data = []
        else:
            with open(self.db_path, 'r') as f:
                try:
                    self.data = load(f)
                except ParserError:
                    self.data = []

    def save(self):
        with open(self.db_path, 'w') as f:
            f.write(dump(self.data))

    def new_result(self, issue_id: str, contact_id: str, phone: str, outcome: str):

        self.data.append({'issue': issue_id,
                          'contact': contact_id,
                          'phone': phone,
                          'result': outcome,
                          'reported': False,
                          'date': datetime.now()})

        self.save()
        self.new_results = True

    def submit_results(self):

        print("Submitting results...")

        for r in self.data:
            if not r['reported']:
                response = requests.post("https://5calls.org/report",
                                         data={'result': r['result'],
                                               'contactid': r['contact'],
                                               'issueid': r['issue'],
                                               'phone': r['phone'],
                                               'via': 'test'
                                               })
                if response.status_code == 200:
                    r['reported'] = True

            self.save()

        self.new_results = False


if __name__ == '__main__':
    cr = CallResults()
    cr.new_result('rec0wRKFr3Z9KsTjy', 'recZhL39WIa4p5MZp', '202-224-5225', 'voicemail')
    cr.submit_results()
