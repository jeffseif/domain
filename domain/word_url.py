import requests

from cachet import sqlite_cache


class WordUrl:

    @classmethod
    @sqlite_cache()
    def raw(cls):
        response = requests.get(cls.URL)
        if response.status_code == requests.codes.ok:
            return response.text

    @classmethod
    def get(cls):
        for line in cls.raw().splitlines():
            if not line.startswith('#'):
                yield line.lower()


class TLD(WordUrl):

    URL = 'http://data.iana.org/TLD/tlds-alpha-by-domain.txt'


class English(WordUrl):

    URL = 'https://raw.githubusercontent.com/jeffseif/junk/master/scrabble.txt'
