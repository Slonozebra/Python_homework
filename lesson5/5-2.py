# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
my_f = open('text_2.txt', 'r', encoding='utf-8')
content_text = my_f.read()
print(content_text)

my_f = open('text_2.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(f'Количество строк в файле - {len(content)}')

my_f = open('text_2.txt', 'r', encoding='utf-8')
content = my_f.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')

f = open('text_2.txt', 'r', encoding='utf-8')
lines = f.readlines()
for num_line, line in enumerate(lines, start=1):
    print ('{} строка содержит - {} слов'.format(num_line, len(line.split())))

my_f.close()
