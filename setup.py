import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-function-cache',
    version='0.1',
    packages=['function_cache'],
    description='A convenience decorator for caching results of functions to various backends.',
    long_description=README,
    author='Yanchuan Sim',
    author_email='yc@botmd.io',
    url='https://gitlab.com/fivehealth/django-function-cache',
    license='Apache License 2.0',
    install_requires=[
        'Django>2.0',
    ]
)
