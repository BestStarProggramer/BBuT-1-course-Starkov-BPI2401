# Задание 1: Открытие и чтение файла

# Чтение всего файла
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Построчное чтение
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())


"""
# Задание 2: Запись в файл

def write_to_file():

    user_text = input("Введите текст для записи в файл: ")
    with open('user_input.txt', 'a') as file:
        file.write(user_text + '\n')
    print("Текст успешно записан.")


# Задание 3: Работа с исключениями

def safe_read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Ошибка: файл {file_name} не существует.")
"""
