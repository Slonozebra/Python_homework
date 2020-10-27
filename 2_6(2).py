# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
goods = []
features = {'Название товара': '', 'Цена': '', 'Количество': '', 'ед.': ''}
analytics = {'Название товара': [], 'Цена': [], 'Количество': [], 'ед.': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для ввода данных нажмите 'Enter', Для просмотра аналитики нажмите 'A'").upper()
    num += 1
    if control == 'A':
        print(f'Аналитика')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')

    for f in features.keys():
        feature_ = input(f'Введите данные "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))









