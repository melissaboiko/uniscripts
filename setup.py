"""setuptools module for uniscripts.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = """Interface to query Unicode UCD script metadata, as per UAX #24.

This module is useful for querying if a text is made of Latin characters,
Arabic, hiragana, kanji (han), and so on.  It works for all scripts supported
by the Unicode character database.

This module is dumb and slow.  If you need speed, you probably want to
implement your own functions.
"""

setup(
    name='uniscripts',

    # PEP440
    version='1.0.1',

    description='query Unicode script metadata',
    long_description=long_description,

    url='https://github.com/leoboiko/uniscripts',

    # Author details
    author='Leonardo Boiko',
    author_email='leoboiko@namakajiri.net',

    # Choose your license
    license='CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',

        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2', # probably?
        'Programming Language :: Python :: 3.3', # I hope...
        'Programming Language :: Python :: 3.4', # actually tested here

    ],

    keywords='unicode script scripts uax24 hiragana katakana kanji han',

    # packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'update']),
    packages=['uniscripts'],

    # cf. https://packaging.python.org/en/latest/requirements.html
    install_requires=[],

    extras_require={},

    package_data={},

    data_files=[],

    entry_points={},
)
