#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='django-edw-fluent',
    version='1.0.1',
    description='Package for connect Django EDW and Django Fluent Pages.',
    author='Infolabs LLC',
    author_email='team@infolabs.ru',
    url='https://github.com/infolabs/django-edw-fluent',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        'Django==2.2.24',
        'django-edw',
        'django-page-builder',
        'django-fluent-pages==1.1.1',
        'django-fluent-contents==1.2',
        'django-constance==1.3.3'
    ],
    dependency_links=[
        'https://github.com/Harut/chakert/tarball/master#egg=chakert-0.2.1'
    ]
)
