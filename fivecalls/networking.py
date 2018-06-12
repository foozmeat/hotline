"""
Provides a layer of indirection for web requests.
"""
import platform
import requests

from fivecalls.gsm_manager import GSMManager


def http_get_json(url, params={}):

    if platform.system() == 'Darwin':
        # Assume a working network stack on a Mac
        try:
            response = requests.get(
                    url=url,
                    params=params,
            )
        except requests.exceptions.RequestException:
            print('HTTP Request failed')
            return False

        if response.ok:
            data = response.json()
            return data
        else:
            return None

    else:
        # On Linux assume that we'll need to fetch via GPRS
        from urllib.parse import urlparse

        phone = GSMManager()
        phone.http_get('ifconfig.co/ip')

