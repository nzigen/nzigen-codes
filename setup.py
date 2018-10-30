# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='nzigen_codes',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/nzigen/nzigen-codes',
      author='ysawa',
      author_email='ysawa@nzigen.com',
      license='MIT',
      packages=[
          'base',
          'encryption',
      ],
      install_requires=[
          'pycrypto',
      ],
      zip_safe=False)
