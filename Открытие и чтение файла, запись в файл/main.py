import os
import time
from pprint import pprint

file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'

def read_cookbook():
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            dish_ingredients = []
            num_ingredients = int(f.readline())
            for i in range(1, num_ingredients+1):
                 ing = f.readline().split(' | ')
                 dish_ingredients.append({'ingredient_name': ing[0], 'quantity': ing[1], 'measure': ing[2].strip()})
            cook_book[line.strip()] = dish_ingredients
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name']not in ingr_list:
                    meas_quan_list['measure'] = ings['measure'].strip()
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name'].strip()] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name'].strip()]['quantity'] = ingr_list[ings['ingredient_name'].strip()]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


def write_func():
    with open(file_name_1, encoding = 'utf8') as f_1:
        text_1 = f_1.read().split('\n')
        text_1.insert(0, str(len(text_1)))
        text_1.insert(0, file_name_1)



    with open(file_name_2, encoding = 'utf8') as f_2:
        text_2 = f_2.read().split('\n')
        text_2.insert(0, str(len(text_2)))
        text_2.insert(0, file_name_2)


    with open(file_name_3, encoding = 'utf8') as f_3:
        text_3 = f_3.read().split('\n')
        text_3.insert(0, str(len(text_3)))
        text_3.insert(0, file_name_3)



    list_1 = [text_1,text_2,text_3]

    list_1.sort(key=len)


    with open('4.txt','a', encoding = 'utf8') as f_4:
        for i in list_1:
            for k in i:
                f_4.write(f'{k}\n')
write_func()



if __name__ == '__main__':
    filename = "recipes.txt"
    cook_book = read_cookbook()
    print('Задание 1------------------------------------------------------------')
    print(f'cook_book = {cook_book}')
    print('Задание 2------------------------------------------------------------')
    pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))
    print('Задание 3------------------------------------------------------------')
    write_func()
