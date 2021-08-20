from country_iterable import CountriesIterable
from md_generator import md_gen
FILE = 'countries.txt'


def countries_exe(file):
    with open(file, 'w', encoding='utf-8') as f:
        for country in CountriesIterable(translation='fra'):
            f.write(f'{" ".join(country)}\n')
            print(country)


def md_gen_exe(file):
    generator = md_gen(file)
    for i in generator:
        print(i.digest())


if __name__ == "__main__":
    countries_exe(FILE)
    md_gen_exe(FILE)

