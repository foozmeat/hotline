import json
from pathlib import Path

import requests

from fivecalls.singleton import Singleton


class FiveCallsModel:

    def __init__(self, **kwargs):

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def __str__(self):
        """ Returns a string representation of TwitterModel. By default
        this is the same as AsJsonString(). """
        return self.AsJsonString()

    def AsJsonString(self) -> str:
        """ Returns the TwitterModel as a JSON string based on key/value
        pairs returned from the AsDict() method. """
        return json.dumps(self.__dict__, sort_keys=True)


class Issue(FiveCallsModel):
    def __init__(self, **kwargs):
        self.id: str = None
        self.name: str = None
        self.script: str = None
        self.reason: str = None
        self.categories: [dict] = []
        self.contacts: [dict] = []
        self.inactive: bool = True
        self.link: str = None
        self.linkTitle: str = None
        self.slug: str = None

        super().__init__(**kwargs)

    def __str__(self):
        return f"({self.id}) {self.name}"


# class Category(FiveCallsModel):
#
#     def __init__(self, **kwargs):
#         self.name: str = None
#         self.issues: [Issue] = []
#
#         super().__init__(**kwargs)


# class Contact(FiveCallsModel):
#
#     def __init__(self, **kwargs):
#         self.id: str = None
#         self.name: str = None
#         self.phone: str = None
#         self.photoURL: str = None
#         self.party: str = None
#         self.state: str = None
#         self.reason = None
#         self.area = None
#         self.field_offices: [dict] = []
#
#         super().__init__(**kwargs)


DATA_PATH = 'data/'
IMAGE_PATH = DATA_PATH + 'images/'
JSON_PATH = DATA_PATH + 'fivecalls.json'


class FiveCallsData(metaclass=Singleton):

    def __init__(self):

        self.issues = []
        self.active_issues = []
        self.categories = {}
        self.contacts = {}
        self.global_count = 0

        if not Path(JSON_PATH).exists():
            self.fetch()

        with open(JSON_PATH, 'r') as fp:
            self._data = json.load(fp)

        for i in self._data['issues']:
            new_issue = Issue(**i)

            if not new_issue.inactive:
                self.active_issues.append(new_issue)

            for c in i['categories']:

                existing_category = self.categories.get(c['name'], None)

                if not existing_category:
                    self.categories[c['name']] = []

                self.categories[c['name']].append(new_issue)

            for c in i['contacts']:
                self.contacts[c['id']] = c

            self.issues.append(new_issue)

        self.global_count = self._data['global_count']

    def fetch(self) -> bool:
        try:
            response = requests.get(
                    url="https://5calls.org/issues/",
                    params={
                        "all": "true",
                        "address": "97211",
                    },
            )
        except requests.exceptions.RequestException:
            print('HTTP Request failed')
            return False

        data = response.json()

        for i in data['issues']:
            for contact in i['contacts']:
                path = IMAGE_PATH + contact['id'] + '.jpg'

                if not Path(path).exists() and contact['photoURL']:

                    try:
                        response = requests.get(contact['photoURL'])

                    except requests.exceptions.RequestException:
                        print('HTTP Request failed')
                        return False
                    else:
                        if response.ok:
                            with open(path, 'wb') as f:
                                f.write(response.content)

        try:
            response = requests.get(
                    url="https://5calls.org/report/",
                    params={},
            )
        except requests.exceptions.RequestException:
            print('HTTP Request failed')
            return False

        else:
            count_data = response.json()
            data['global_count'] = int(count_data['count'])

        with open(JSON_PATH, 'w') as fp:
            json.dump(data, fp)

        return True


if __name__ == '__main__':
    fcd = FiveCallsData()
    print(f"issues: {len(fcd.issues)}")
    print(f"active issues: {len(fcd.active_issues)}")
    print(f"categories: {len(fcd.categories)}")
