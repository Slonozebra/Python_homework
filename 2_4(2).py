# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

new_str = input("Напишите несколько слов через пробел: ")
new_word = []
num = 1
for el in range(new_str.count(' ') + 1):
    new_word = new_str.split()
    if len(str(new_word)) <= 10:
        print(f" {num} {new_word [el]}")
        num += 1
    else:
        print(f" {num} {new_word [el] [0:10]}")
        num += 1