import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='function-cache',
    version='0.1.7',
    packages=['function_cache'],
    description='A Django-based convenience decorator for caching results of functions to various backends.',
    long_description=README,
    long_description_content_type='text/markdown',
    author='5 Health Inc',
    author_email='hello@botmd.io',
    url='https://github.com/fivehealth/function-cache',
    license='MIT License',
    install_requires=[
        'Django>2.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
    ],
)
