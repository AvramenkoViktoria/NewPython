from app.io.input import input_from_console, input_from_file_builtin, input_from_file_pandas
from app.io.output import output_to_console, output_to_file_builtin

def main():
    # Шляхи до файлів
    file_builtin_input = "data/input_builtin.txt"
    file_pandas_input = "data/input_pandas.csv"
    file_output = "data/output.txt"

    # Отримання текстів
    text1 = input_from_console()
    text2 = input_from_file_builtin(file_builtin_input)
    text3 = input_from_file_pandas(file_pandas_input)

    # Вивід у консоль
    output_to_console("\n--- Текст з консолі ---")
    output_to_console(text1)

    output_to_console("\n--- Текст з файлу (builtin) ---")
    output_to_console(text2)

    output_to_console("\n--- Текст з файлу (pandas) ---")
    output_to_console(text3)

    # Запис до файлу
    output_to_file_builtin("=== Текст з консолі ===", file_output)
    output_to_file_builtin(text1, file_output)

    output_to_file_builtin("=== Текст з файлу (builtin) ===", file_output)
    output_to_file_builtin(text2, file_output)

    output_to_file_builtin("=== Текст з файлу (pandas) ===", file_output)
    output_to_file_builtin(text3, file_output)


if __name__ == "__main__":
    main()
