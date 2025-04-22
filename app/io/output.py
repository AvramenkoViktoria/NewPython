import pandas as pd

def output_to_console(text):
    """
    Функція для виводу тексту у консоль
    :param text: текст для виводу
    """
    print(text)

def output_to_file_builtin(text, filepath):
    """
    Функція для запису тексту у файл за допомогою вбудованих можливостей Python
    :param text: текст для запису
    :param filepath: шлях до файлу
    """
    # Якщо text є DataFrame, перетворюємо його на рядок
    if isinstance(text, pd.DataFrame):
        text = text.to_string(index=False)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)