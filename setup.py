import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='function-cache',
    version='0.1',
    packages=['function_cache'],
    description='A Django-based convenience decorator for caching results of functions to various backends.',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Yanchuan Sim',
    author_email='yc@botmd.io',
    url='https://gitlab.com/fivehealth/function-cache',
    license='Apache License 2.0',
    install_requires=[
        'Django>2.0',
    ]
)
