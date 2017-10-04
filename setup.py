from setuptools import setup

from domain import __author__
from domain import __email__
from domain import __program__
from domain import __url__
from domain import __version__


setup(
    author=__author__,
    author_email=__email__,
    dependency_links=[],
    install_requires=[
        'requests>=2.9.1',
    ],
    name=__program__,
    packages=[__program__],
    platforms='all',
    setup_requires=[
        'setuptools',
        'tox',
    ],
    test_suite='tests',
    url=__url__,
    version=__version__,
)
