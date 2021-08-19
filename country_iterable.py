import requests
import urllib

URL = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
TRANSLATIONS = ['rus', 'deu', 'fra', 'eng'] #все не брал т.к. было лень


def create_wiki_url(name, translation='eng'):
    name = urllib.parse.quote("_".join(name.split()))
    url = f'https://{translation[:-1]}.wikipedia.org/wiki/{name}'
    return url


def get_name(country, translation):
    if translation == 'eng':
        return country['name']['official']
    return country['translations'][translation]['common']


class CountryIterator:
    def __init__(self, countries, translation='eng'):
        self.countries = countries
        self.cursor = 0
        self.limit = len(countries)
        self.translation = translation

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor >= self.limit:
            raise StopIteration

        name = get_name(self.countries[self.cursor], self.translation)
        self.cursor += 1
        return name, create_wiki_url(name, self.translation)


class CountriesIterable:
    def __init__(self, url=URL, translation='eng'):
        if translation not in TRANSLATIONS:
            raise ValueError(f'не найден язык {translation} в {str(TRANSLATIONS)}')
        self.translation = translation
        self.countries = requests.get(url).json()

    def __iter__(self):
        return CountryIterator(self.countries, self.translation)

    def __str__(self):
        return str([i for i in self])
