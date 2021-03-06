import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='function-cache',
    version='0.2.0',
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
    python_requires='>=3',
    keywords='django cache',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'License :: OSI Approved :: MIT License',
    ],
)
