import json


class Wiki:

    def __init__(self, file_path):
        self.file_path = file_path

    def func(self, path):
        with open(self.file_path, 'rt', encoding='utf-8') as file:
            countries_list = json.load(file)
            names = list()
            for country in countries_list:
                name = country['name']['common']
                names.append(name)
        wiki_links = dict()
        with open(path, 'wt', encoding='utf-8') as new_file:
            for item in names:
                wiki_links[item] = 'https://en.wikipedia.org/wiki/' + str(item).replace(' ', '_')
            json.dump(wiki_links, new_file, ensure_ascii=False, indent=4)
            print(f'\n Файл {path} сохранён \n')
