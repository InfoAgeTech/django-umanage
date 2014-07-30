from __future__ import unicode_literals

import os

from setuptools import find_packages
from setuptools import setup
from umanage import APP_URL


classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='django-umanage',
    version='0.0.1',
    description='Django notifications app for django',
    long_description=README,
    author='Troy Grosfield',
    maintainer='Troy Grosfield',
    url=APP_URL,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'django >= 1.5.8',
        'markdown'
    ],
    test_suite='nose.collector',
    tests_require=[
        'django_nose'
    ],
    classifiers=classifiers
)
