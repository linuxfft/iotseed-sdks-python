# -*- coding: utf-8 -*-
"""
IOTSeedSDK
-----

IOTSeedSDK 作为对接IOTSeed IOT平台的Python客户端开发包


IOTSeedSDK 安装非常方便
`````````````````

And run it:

.. code:: bash

    $ pip install IOTSeedSDK

"""
import re
import ast
from setuptools import setup
import sys


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('IOTSeedSDK/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

required_list = [
        'AWSIoTPythonSDK>=1.3.1',
        'tzlocal>=1.5.1',
    ]

setup(
    name='IOTSeedSDK',
    version=version,
    url='http://github.com/masami10/iotseed-sdks-python/',
    license='MIT',
    author='frank gu',
    author_email='support@cloudahead.net',
    description='IOTSeedSDK 作为对接IOTSeed IOT平台的Python客户端开发包',
    long_description=__doc__,
    packages=['IOTSeedSDK'],
    keywords=['IOTSeed', 'iot', 'mqtt'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=required_list,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)