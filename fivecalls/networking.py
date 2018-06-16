"""
Provides a layer of indirection for web requests.
"""
import sys
import requests

from fivecalls.gsm_manager import SIM8XXManager


def http_get_json(url, params={}):
    phone = SIM8XXManager()
    data = None

    if sys.platform == 'linux':
        phone.ppp_up()

    try:
        response = requests.get(
                url=url,
                params=params,
        )
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return False

    else:
        if response.ok:
            data = response.json()

    finally:
        if sys.platform == 'linux':
            phone.ppp_down()

        return data
