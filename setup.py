# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='nzigen_low_level',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/nzigen/nzigen-low-level-python',
      author='Yoshihiro Sawa',
      author_email='ysawa@nzigen.com',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      test_suite='test',
      install_requires=[
          'pycrypto',
      ],
      zip_safe=True)
