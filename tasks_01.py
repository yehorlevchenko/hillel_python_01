from collections import OrderedDict
from statistics import mean
import pandas as pd

def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    # my code here
    result_list = [i for i in url_list if 'catalog' in i]
    return result_list


def idiotic_str(input_str):
    """
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """
    # my code here
    idiotic_str = ''
    i = True
    for char in input_str:
        if i:
            idiotic_str += char.lower()
            i = False
        else:
            idiotic_str += char.upper()
            i = True
    return idiotic_str
idiotic_str('hello world')


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    # my code here
    try:
        for char in input_str:
            if len(input_str)%2 == 0:
                output_str = input_str[len(input_str)//2-1] + \
                input_str[len(input_str)//2]
            elif len(input_str) != 0:
                output_str = input_str[len(input_str)//2-1] + \
                input_str[len(input_str)//2] + \
                input_str[len(input_str)//2+1]
        return output_str
    except IndexError:
        print('The word must be at least 2 letters long')
get_str_center('abracadabra')


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    # my code here
    output_dict = {char:input_str.count(char) for char in input_str}
    return output_dict
count_symbols('abracadabra')


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    # my code here
    result_str = str1[:len(str1)//2] + str2 + str1[len(str1)//2:]
    return result_str
mix_strings('house','adorable')


def avg_score(score_list):
    """
    Дописать функцию, которая принимает список строк с оценками, а возвращает
    список строк со средним баллом
    Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
    ["Mike|65", "Jane|42"]
    """
    # my code here
    # First, break down score_list into two 'names' list & 'scores' list.
    # Then, calculate mean values in 'scores'.
    # Finally, contatenate two lists to return 'avg_scores'
    
    names = [score_list[i].split('|')[:1] for i in range(len(score_list))]
    names = [i for sublist in names for i in sublist] # flat list of names
    
    scores = [score_list[i].split('|')[1:] for i in range(len(score_list))]
    scores = [j.split(',') for i in scores for j in i]  # nested list of str
    avg = [str(mean([int(i) for i in sublist])) for sublist in scores]

    avg_scores = [name+'|'+v for name,v in zip(names,avg)]
    return avg_scores

avg_score(["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"])


def encrypt_str(input_str):
    """
    Дописать функцию, которая будет шифровать полученную строку следующим
    образом:
    Пример 1: "www" -> "w3"
    Пример 2: "abbbccdeffgggg" -> "ab3c2def2g4"
    """
    # my code here
    
    # Hence there is no OrderedSet object in Python, 
    # we fake it with OrderedDict object in order to get unique values 
    # from input_str & preserve their order
    
    uique_chars = OrderedDict((key,True) for key in input_str)  # OrderedDict
    list1 = list(uique_chars.keys())      # list of characters
    
    occurences = {char:input_str.count(char) for char in input_str} # dict
    list2 = list(occurences.values())    # list of occurences (int)
    list2 = list(map(str,list2))        # list of occurences (str)
    
    # element wise concatenation from list1 & list2
    concat_list = [char+number for char,number in zip(list1,list2)]
    encrypted_str = ''.join(concat_list)    # final result
    return encrypted_str
encrypt_str('abbbccdeffgggg')


def square_dict(input_dict):
    """
    Сгенерировать dict() из списка ключей ниже по формуле (key : key*key).
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
    """
    # no addit. code needed; call the func using the list 'keys' as arg
    squared_dict = {key:key**2 for key in input_dict}
    return squared_dict
square_dict([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    # my code here
    even_int_list = [i for i in range(0,101) if i%2 == 0]
    return even_int_list
even_int_generator()


def replace_vowels(input_str,vowel):
    """
    Заменить в произвольной строке согласные буквы на гласные.
    """
    # my code here
    vowels = ['a','e','i','o','u','y']
    result_list = []
    for char in input_str.lower():
        if char in vowels:
            result_list.append(char)
        elif char not in vowels:
            result_list.append(vowel)
    result_str = ''.join(result_list)
    return result_str
replace_vowels('Darling','i')


def filter_unique_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """
    # my code here
    unique_int_list = list(set(input_list))
    return unique_int_list


def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    # my code here
    biggest_ints = sorted(set(input_list), reverse=True)
    biggest_ints = biggest_ints[:3]
    return biggest_ints


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    # my code here
    lowest_int_index = input_list.index(min(input_list))
    return lowest_int_index


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    # my code here
    reversed = input_list[::-1]
    return reversed


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    # my code here
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    common_keys = keys1.intersection(keys2)
    return common_keys


def sort_by_age(student_list):
    """
    Дан массив из словарей. C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
        {'Kiev': [ {'name': 'Viktor', 'age': 30 },
                  {'name': 'Andrey', 'age': 34}],
        'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                  {'name': 'Artem', 'age': 50}],
        'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                 {'name': 'Dmitriy', 'age': 21}]}
    """
    # my code here
    # Create pandas DataFrame object;
    # sort 'age' as a column in DataFrame;
    # use .groupby() + .get_group() in order to obtain the desired outcome
    
    df = pd.DataFrame(student_list)
    df = df.sort_values(by=['age'])
    df = df.groupby(['city'])
    groups_list = list(df.groups.keys())
    sorted_dict = {}   
    for elem in groups_list:
        sorted_dict[elem] = df.get_group(elem)[['name','age']].to_dict('records')
    return sorted_dict

sort_by_age([{'name': 'Viktor','city':'Kiev','age':30}, \
             {'name': 'Maksim','city':'Dnepr','age': 20},\
             {'name': 'Vladimir','city':'Lviv','age': 32 },\
             {'name': 'Andrey','city':'Kiev','age': 34},\
             {'name': 'Artem','city':'Dnepr','age': 50},\
             {'name': 'Dmitriy','city':'Lviv','age': 21}])
