# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='agilent_34411a',
      version = '0.2.0',
      description = 'Interface to the table-top DMM Agilent 34411A via TCP/IP',
      long_description = '',
      author = 'Philipp Klaus',
      author_email = 'klaus@physik.uni-frankfurt.de',
      url = '',
      license = 'GPL',
      packages = ['agilent_34411a'],
      entry_points = {
        'console_scripts': [
          'agilent_34411a_cli = agilent_34411a.cli:main',
        ],
      },
      zip_safe = True,
      platforms = 'any',
      keywords = 'Agilent 34411A DMM',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GPL License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Logging',
      ]
)


