import hashlib


def hashlines(path):
    with open(path, 'rt', encoding='utf-8') as file:
        print(f'\n *****Ниже будут выведены md5 хеши каждой строки файла {path}***** \n')
        for line in file.readlines():
            hashed_line = hashlib.md5(line.encode('utf-8')).hexdigest()
            print(hashed_line)



