from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='TwoCaptcha',
    version='0.0.1',
    description='2Captcha Python3 API Wrapper',
    long_description=long_description,
    url='https://github.com/My-kal/2Captcha',
    author='Mykal Burris',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='2captcha development',
    packages=find_packages(),
    install_requires=['requests']
)