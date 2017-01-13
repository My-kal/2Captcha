# twocaptcha/__init__.py

# TODO:
# [x] proxy support
# [] poll interval
# [x] get balance
# [] error handling
# [] request unblocking


from requests import Session
from time import sleep
import os

# API_KEY = os.environ.get('API_KEY', None)
# 'https://2captcha.com/setting'

class TwoCaptcha(object):
    """Interface for 2Captcha API."""
    BASE_URL = 'http://2captcha.com'

    def __init__(self, api_key):
        self.session = Session()
        self.session.params = {'key': api_key}

    def solve_recaptcha(self, site_url, site_key, proxy=None, poll=None):
        """
        :param site_url: domain of the site with recaptcha
        :param site_key: open key on site, can be found in html source
        :param proxy
        :return: recaptcha token
        """

        payload = {
            'googlekey': 'site_key',
            'pageurl': site_url,
            'method': 'userrecaptcha'
        }

        # post site key to get captcha ID
        if proxy:
            req = session.post('http://2captcha.com/in.php', params=payload, proxies=proxy)
        else:
            req = session.post('http://2captcha.com/in.php', params=payload)

        captcha_id = req.text.split('|')[1]

        # retrieve response [recaptcha token]
        payload = {}
        payload['id'] = captcha_id
        payload['action'] = 'get'

        if proxy:
            req = session.get('http://2captcha.com/res.php', params=payload, proxies=proxy)
        else:
            req = session.get('http://2captcha.com/res.php', params=payload)


        recaptcha_token = req.text
        while 'CAPCHA_NOT_READY' in recaptcha_token:
            sleep(5)
            req = session.get('http://2captcha.com/res.php', params=payload)
        recaptcha_token = recaptcha_token.split('|')[1]
        return recaptcha_token

    def get_balance(self):
        """
        :return: account balance in USD
        """
        payload = {
            'action': 'getbalance',
            'json': 1,
        }
        response = session.get(url=BASE_URL + '/res.php', params=payload)
        JSON = response.json()
        if JSON['status'] == 1:
            balance = JSON['request']
            return balance
