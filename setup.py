"""
setuptools module for uniscripts.
"""
from pathlib import Path
import re
from setuptools import setup, find_packages

PACKAGE_NAME = "uniscripts"

# Load version from __init__.py
with open(f"{PACKAGE_NAME}/unidata.py", encoding="utf-8") as f:
    version = re.search(r'^__unicode_version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

# Load load description from README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Load requirements (if any) from requirements.txt
requirements = []
try:
    with open('requirements.txt', encoding="utf-8") as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

setup(
    name=PACKAGE_NAME,
    version=version,
    description='Obtain name of Unicode scripts used in text',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,

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
        'Development Status :: 5 - Production/Stable',

        "Intended Audience :: Developers",
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Localization',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',

        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        "Operating System :: OS Independent",

        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",

    ],

    keywords='unicode script scripts uax24 hiragana katakana kanji han',
)
