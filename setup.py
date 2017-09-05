import os

from setuptools import setup, find_packages

version = __import__('demo').__version__

reqs = [line.strip() for line in open('requirements.txt')]

DESCRIPTION = (
    '''PyWPS is an implementation of the Web Processing Service standard from the
Open Geospatial Consortium. PyWPS is written in Python.

This Demo is an example service using the PyWPS server, distributed along
with a basic set of sample processes and sample configuration file. It's
usually used for training and development purposes.
''')

KEYWORDS = 'Birdhouse PyWPS WPS OGC processing'

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: GIS',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
]

setup(name='demo',
      version=version,
      description=DESCRIPTION,
      classifiers=classifiers,
      author='Birdhouse',
      author_email='wps@dkrz.de',
      url='https://github.com/bird-house/birdhouse-workshop',
      license="Apache License v2.0",
      keywords=KEYWORDS,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='demo',
      install_requires=reqs,
      entry_points={
          'console_scripts': [
             'demo=demo:main'
          ]
      },
      )
