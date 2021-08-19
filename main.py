from country_iterable import CountriesIterable
FILE = 'countries.txt'


def countries_exe(file):
    with open(file, 'w', encoding='utf-8') as f:
        for country in CountriesIterable(translation='fra'):
            f.write(f'{" ".join(country)}\n')


if __name__ == "__main__":
    countries_exe(FILE)
