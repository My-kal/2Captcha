TwoCaptcha
==========

2Captcha Python3 API Wrapper

Prerequisites
-------------

You will need a ``2Captcha API Key`` which can be found `here`_ after
registering for 2Captcha on https://2captcha.com

Usage
-----

TwoCaptcha
~~~~~~~~~~

.. code:: py

    from twocaptcha import TwoCaptcha

    API_KEY = 'YOUR_API_KEY_HERE'
    twoCaptcha = TwoCaptcha(API_KEY)

TwoCaptcha.solve\_captcha
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: py

    page_url = 'http://www.example.com'
    site_key = '6Le4AQgUAAAAAABhHEq7RWQNJwGR_M-6Jni9tgtA'
    captcha_token = twoCaptcha.solve_captcha(site_key=site_key, page_url=page_url)
    print(captcha_token) # Ex. '03AE...'

TwoCaptcha.get\_balance
~~~~~~~~~~~~~~~~~~~

.. code:: py

    balance = twoCaptcha.get_balance()
    print(balance) # Ex. '6.11472'

TODO:
-----

-  [ ] proxy support
-  [ ] poll interval
-  [ ] request error handling
-  [ ] request unblocking
-  [ ] unit tests

.. _here: https://2captcha.com/setting