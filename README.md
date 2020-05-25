# Advanced Python 01
Это репозиторий с домашними заданиями курса Advanced Python.
def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    return [i for i in url_list if '/catalog/' in i]

#print(catalog_finder())





def idiotic_str(input_str):
    """
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """
    idiotic_str = ''
    for i in input_str:
        idiotic_str += i.upper() if len(idiotic_str) % 2 else i
    return idiotic_str

#print(idiotic_str())


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    str = len(input_str) // 2
    out = input_str[str - 1: 1 - str]
    return out


print(get_str_center(input_str="gggddgdaaaggg"))


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    out = dict()
    for i in input_str:
        out.update({i: out.get(i, 0) + 1})
    return out

# print(count_symbols())


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    return str1[:(len(str1) // 2)] + str2 + str1[(len(str1) // 2):]


print(mix_strings(str1='sdfsdfpgsq', str2='sadjsdaqw'))


def avg_score(score_list):
    """
    Дописать функцию, которая принимает список строк с оценками, а возвращает
    список строк со средним баллом
    Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
    ["Mike|65", "Jane|42"]
    """
    # Я не знал, как сделать эту функцию, поэтому это код с занятия, можешь миносовать балл:)
    avg_scores = list()
    for student in score_list:
        name, str_scores = student.split('|')
        scores_list = str_scores.split(', ')
        scores = [int(score) for score in scores_list]
        avg_score = f'{name}|{sum(scores) // len(scores)}'
        avg_scores.append(avg_score)
    return avg_scores

# print(avg_score())


def encrypt_str(str, key):
    """
    Дописать функцию, которая будет шифровать полученную строку следующим
    образом:
    Пример 1: "www" -> "w3"
    Пример 2: "abbbccdeffgggg" -> "ab3c2def2g4"
    """
    strg = " "
    for letter in str:
        strg += chr(ord(letter) ^ key)
    return strg


parol = input("Введите пароль:")
key = 8
print("Оригинал:", parol)
encr_strg = encrypt_str(parol, key)
print("Зашифрованный:", encr_strg)
print("Расшифрованный:", encrypt_str(encr_strg, key))


def square_dict(input_dict):
    """
    Сгенерировать dict() из списка ключей ниже по формуле (key : key*key).
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
    """
    return {key: key * key for key in input_dict}


print(square_dict(input_dict=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    return [i for i in range(0, 100, 2)]


print(even_int_generator())


def replace_vowels():
    """
    Заменить в произвольной строке согласные буквы на гласные.
    """
    str = "AABABBAABBBAB"
    return str.replace("AABABBAABBBAB", "BBABAABBAAABAB")


print(replace_vowels())


def filter_unique_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """
    return list(set(input_list))


print(filter_unique_int(input_list=[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))


def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    return sorted(set(input_list))[-3:]
    #return input_list.index(max(input_list))

print(three_biggest_int(input_list=[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    return input_list.index(min(input_list))


print(lowest_int_index(input_list=[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    return list(reversed(input_list))


print(reversed_list(input_list=[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    list_1 = list(dict1.keys())
    list_2 = list(dict2.keys())
    list_values = []

    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                list_values.append(dict1.get(list_1[i]))
                list_values.append(dict2.get(list_2[i]))

    return list_values

# print(find_common_keys())


def sort_by_age(student_list):
    """
    Дан массив из словарей. C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
        {
           'Kiev': [ {'name': 'Viktor', 'age': 30 },
                        {'name': 'Andrey', 'age': 34}],
           'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                           {'name': 'Artem', 'age': 50}],
           'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                        {'name': 'Dmitriy', 'age': 21}]
        }
    """
    sorted_dict = None
    return sorted_dict
