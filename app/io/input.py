import pandas as pd

def input_from_console():
    """
    Функція для вводу тексту з консолі
    """
    return input("Введіть текст: ")


def input_from_file_builtin(filepath):
    """
    Функція для зчитування з файлу за допомогою вбудованих можливостей Python
    :param filepath: шлях до файлу
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def input_from_file_pandas(filepath):
    """
    Функція для зчитування з файлу за допомогою бібліотеки pandas
    :param filepath: шлях до файлу
    """
    return pd.read_csv(filepath)

