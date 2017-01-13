# TwoCaptcha
Python wrapper for 2Captcha API


# Prerequisites:
2Captcha API key; after registering it can be found
here: https://2captcha.com/setting

# Usage:

## Solve ReCaptcha
```
from twocaptcha import TwoCaptcha

SITE_URL = 'http://www.example.com'
SITE_KEY = '6Le4AQgUAAAAAABhHEq7RWQNJwGR_M-6Jni9tgtA'

twoCaptcha = TwoCaptcha(<API_KEY>)
recaptcha_token = twoCaptcha.solve_recaptcha(site_url=SITE_URL, site_key=SITE_KEY)
```

## Get Account Balance
```
from twocaptcha import TwoCaptcha

twoCaptcha = TwoCaptcha(<API_KEY>)
balance = twoCatpcha.get_balance()
```

## TODO:
- [] proxy support
- [] poll interval
- [] request error handling
- [] request unblocking
- [] unit tests
