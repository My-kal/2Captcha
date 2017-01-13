#/twocaptcha/twocaptcha.py

# TODO:
# [] proxy support

from .init import session
from time import sleep


class TwoCaptcha(object):
    def __init__(self):
        pass

    def solve_recaptchaV2(self, site_url, site_key):
        payload = {}
        payload['googlekey'] = site_key
        payload['pageurl'] = site_url
        payload['method'] = 'userrecaptcha'

        # # post site key to get captcha ID
        # req = session.post('http://2captcha.com/in.php', params=payload)
        # captcha_id = req.text.split('|')[1]
        #
        # # retrieve response [recaptcha token]
        # payload = {}
        # payload['id'] = captcha_id
        # payload['action'] = 'get'
        #
        # req = session.get('http://2captcha.com/res.php', params=payload)
        # recaptcha_token = req.text
        # while 'CAPCHA_NOT_READY' in recaptcha_token:
        #     sleep(5)
        #     req = session.get('http://2captcha.com/res.php', params=payload)
        # recaptcha_token = recaptcha_token.split('|')[1]
        # return recaptcha_token
        
        return {
            'site_key': site_key,
            'site_url': site_url
        }
