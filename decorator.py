from datetime import datetime
import time
import json
import hashlib

# ЗАДАЧА 1


def logger(old_function):
    logs = list()

    def new_function(*args):
        result = old_function(*args)
        date_and_time = datetime.now().strftime('%d/%m/%y %H:%M:%S')
        logs.append(
            f'Дата и время вызова: {date_and_time}, '
            f'имя функции: {old_function.__name__}, '
            f'аргументы: {args}, '
            f'возвращено значение: {result}'
        )
        with open('logs.json', 'wt', encoding='utf-8') as file:
            json.dump(logs, file, ensure_ascii=False, indent=4)
            print(f'{date_and_time} Данные о вызове функции {old_function.__name__} записаны в файл logs.json')
        time.sleep(1)
        return result
    return new_function


@logger
def sum_func(a, b):
    return a + b


sum_func(2, 2)
sum_func(5, 5)


# ЗАДАЧА 2

def parametrized_logger(file_path):
    parametrized_logs = list()

    def logger_decorator(old_function):

        def new_function(*args):
            result = old_function(*args)
            date_and_time = datetime.now().strftime('%d/%m/%y %H:%M:%S')
            parametrized_logs.append(
                f'Дата и время вызова: {date_and_time}, '
                f'имя функции: {old_function.__name__}, '
                f'аргументы: {args}, '
                f'возвращено значение: {result}'
            )
            if file_path:
                with open(file_path, 'wt', encoding='utf-8') as file:
                    json.dump(parametrized_logs, file, ensure_ascii=False, indent=4)
                    print(
                        f'{date_and_time} Данные о вызове функции {old_function.__name__} '
                        f'записаны в файл {file_path}'
                    )
            elif not file_path:
                with open('logs.json', 'wt', encoding='utf-8') as default_file:
                    json.dump(parametrized_logs, default_file, ensure_ascii=False, indent=4)
                    print(f'{date_and_time} Данные о вызове функции {old_function.__name__} записаны в файл logs.json')
            time.sleep(1)
            return result

        return new_function

    return logger_decorator


@parametrized_logger('my_logs.json')
def sum_func(a, b):
    return a + b


sum_func(2, 2)
sum_func(3, 3)


# ЗАДАЧА 3


@parametrized_logger('hashlines_generator_logs.json')
def hashlines(path):
    with open(path, 'rt', encoding='utf-8') as file:
        print(f'\n *****Ниже будут выведены md5 хеши каждой строки файла {path}***** \n')
        for line in file.readlines():
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


for item in hashlines('wikipedia.json'):
    print(item)

