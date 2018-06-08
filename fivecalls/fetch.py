import json
from pathlib import Path

import requests

from fivecalls.data import JSON_PATH, IMAGE_PATH


def fetch() -> bool:
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
    fetch()
