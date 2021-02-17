import json


class Wiki:

    def __init__(self, file_path, new_path):
        self.file_path = file_path
        self.new_path = new_path
        self.index_count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index_count += 1
        with open(self.file_path, 'rt', encoding='utf-8') as file:
            countries_list = json.load(file)
            names = list()
            for country in countries_list:
                name = country['name']['common']
                names.append(name)
            wiki_links = dict()
            with open(self.new_path, 'wt', encoding='utf-8') as new_file:
                for item in names:
                    wiki_links[item] = 'https://en.wikipedia.org/wiki/' + str(item).replace(' ', '_')
                json.dump(wiki_links, new_file, ensure_ascii=False, indent=4)
        if self.index_count == len(names):
            raise StopIteration
        return f'\n Ссылка на страну {names[self.index_count]} сохранена в файл {self.new_path} \n'

