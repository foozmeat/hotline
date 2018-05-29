import json
import sys
from pathlib import Path

import requests

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
    sys.exit(1)

data = response.json()

with open('data/fivecalls.json', 'w') as fp:
    json.dump(data, fp)

for i in data['issues']:
    for contact in i['contacts']:
        id = contact['id']
        path = f'data/images/{id}'

        if not Path(path).exists() and contact['photoURL']:

            try:
                response = requests.get(contact['photoURL'])

            except requests.exceptions.RequestException:
                print('HTTP Request failed')
                sys.exit(1)
            else:
                if response.ok:
                    with open(path, 'wb') as f:
                        f.write(response.content)

# issues = []
# active_issues = []
# categories = {}
# contacts = {}
#
# for i in data['issues']:
#     new_issue = Issue(**i)
#
#     issues.append(new_issue)
#
#     if not new_issue.inactive:
#         active_issues.append(new_issue)
#
#     for c in i['categories']:
#
#         existing_category = categories.get(c['name'], None)
#
#         if not existing_category:
#             categories[c['name']] = []
#
#         categories[c['name']].append(new_issue)
#
#     for c in i['contacts']:
#
#         contacts[c['id']] = c
#
# pp.pprint(categories)
# # pp.pprint(issues[0].__dict__)
# # pp.pprint(contacts)
