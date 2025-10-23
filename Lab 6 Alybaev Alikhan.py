                                                                     # Alybaev Alikhan Lab 6
# Python builtin functions exercises
# Task 1:
import math 

numbers = [2, 3, 4, 5]  
result = math.prod(numbers)

print("Произведение чисел в списке: ", result)

# Task 2:
text = input("Введите строку: ")

upper_count = sum(1 for char in text if char.isupper()) 
lower_count = sum(1 for char in text if char.islower())  

print("Количество заглавных букв:", upper_count)
print("Количество строчных букв:", lower_count)

# Task 3:
text = input("Введите строку: ")

cleaned_text = ''.join(text.lower().split())

if cleaned_text == cleaned_text[::-1]:
    print("Это палиндром.")
else:
    print("Это не палиндром.")

# Task 4:
import time
import math

number = int(input("Введите число: "))
milliseconds = int(input("Введите миллисекунды: "))

time.sleep(milliseconds / 1000)

result = math.sqrt(number)

print(f"Корень числа {number} после {milliseconds} миллисекунд равен {result}")

# Task 5:
my_tuple = (True, 1, "Hello", 5)

result = all(my_tuple)

print("Все элементы кортежа являются истинными:", result)

# Python Directories and Files exercises
# Task 1:
import os

path = input("Введите путь к директории: ")

if os.path.exists(path):
    print("\nТолько директории:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nТолько файлы:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nВсе элементы (файлы и директории):")
    for item in os.listdir(path):
        print(item)
else:
    print("Указанный путь не существует.")

# Task 2:
import os

path = input("Введите путь: ")

print("\nРезультат проверки:")

print("Существует:", os.path.exists(path))

print("Доступно для чтения:", os.access(path, os.R_OK))

print("Доступно для записи:", os.access(path, os.W_OK))

print("Доступно для выполнения:", os.access(path, os.X_OK))

# Task 3:
import os

path = input("Введите путь: ")

if os.path.exists(path):
    print("Путь существует.")
    
    filename = os.path.basename(path)
    print("Имя файла (если есть):", filename)
    
    directory = os.path.dirname(path)
    print("Путь к директории:", directory)

else:
    print("Путь не существует.")

# Task 4:
file_path = input("Введите путь к текстовому файлу: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines() 
        print("Количество строк в файле:", len(lines))  
except FileNotFoundError:
    print("Файл не найден. Проверьте путь.")

# Task 5:
my_list = ["apple", "banana", "cherry", "orange"]

file_path = "output.txt"

with open(file_path, 'w', encoding='utf-8') as file:
    for item in my_list:
        file.write(item + "\n")  

print(f"Список успешно записан в файл {file_path}")

# Task 6:
import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"Это файл {filename}")  
    print(f"Создан файл: {filename}")

# Task 7:
source_file = input("Введите имя исходного файла: ")
destination_file = input("Введите имя файла, в который нужно скопировать содержимое: ")

try:
    with open(source_file, 'r', encoding='utf-8') as src:
        content = src.read()

    with open(destination_file, 'w', encoding='utf-8') as dst:
        dst.write(content)

    print(f"Содержимое файла '{source_file}' успешно скопировано в '{destination_file}'.")

except FileNotFoundError:
    print("Ошибка: исходный файл не найден.")
except Exception as e:
    print("Произошла ошибка:", e)

# Task 8:
import os

file_path = input("Введите путь к файлу для удаления: ")

if os.path.exists(file_path):
    print("Файл существует.")

    if os.access(file_path, os.W_OK):
        try:
            os.remove(file_path)  
            print("Файл успешно удалён.")
        except Exception as e:
            print("Ошибка при удалении файла:", e)
    else:
        print("Нет прав на удаление файла (доступ к записи запрещён).")
else:
    print("Файл по указанному пути не существует.")