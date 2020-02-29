from random import randint


def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    # your code here
    result_list = None
    return result_list


def idiotic_str(input_str):
    """
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """
    r = ''
    for i, c in enumerate(input_str):
        i += 1
        r += c if i % 2 else c.upper()
    return r

    # idiotic_str = None
    # return idiotic_str


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    st = ''
    if len(input_str) % 2 == 0:
        st = input_str[int(len(input_str) / 2 - 1)] + input_str[int(len(input_str) / 2)]
    else:
        st = input_str[int(len(input_str) // 2 - 1)] + input_str[int(len(input_str) // 2)] + input_str[
            int(len(input_str) // 2 + 1)]

    return st

    # output_str = None
    # return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    d1 = dict.fromkeys([chr(x1) for x1 in range(65, 90)], 0)
    d2 = dict.fromkeys([chr(x1) for x1 in range(97, 122)], 0)
    d1.update(d2)
    for i in range(len(input_str)):
        if ((ord(input_str[i]) >= 65) and (ord(input_str[i]) <= 90)) or (
                (ord(input_str[i]) >= 97) and (ord(input_str[i]) <= 122)):
            d1[input_str[i]] += 1

    return d1

    # output_dict = None
    # return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    x = ''
    x = str1[:(len(str1) // 2)] + str2 + str1[(len(str1) // 2):]

    return x

    # result_str = None
    # return result_str


def avg_score(score_list):
    """
    Дописать функцию, которая принимает список строк с оценками, а возвращает
    список строк со средним баллом
    Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
    ["Mike|65", "Jane|42"]
    """
    first_sort = []
    for i in range(len(score_list)):
        first_sort += score_list[i].split('|')

    second_sort = []
    for i in range(len(first_sort)):
        second_sort += first_sort[i].split(',')

    print(second_sort)

    students_rating = []
    average_mark = 0
    for i in range(0, len(second_sort), 5):
        average_mark = (int(second_sort[i + 1]) + int(second_sort[i + 2]) + int(second_sort[i + 3]) + int(second_sort[i + 4])) / 4
        print(second_sort[i])
        st = (second_sort[i] + '|' + str(average_mark))
        students_rating.append(st)

    return students_rating


    # avg_scores = None
    # return avg_scores


def encrypt_str(input_str):
    """
    Дописать функцию, которая будет шифровать полученную строку следующим
    образом:
    Пример 1: "www" -> "w3"
    Пример 2: "abbbccdeffgggg" -> "ab3c2def2g4"
    """
    k = 0
    letter = ''
    while True:
        if k >= len(input_str):
            break
        counter = 0
        letter = input_str[k]
        for j in range(len(input_str)):
            if letter == input_str[j]:
                counter += 1
            else:
                continue
        if counter == 1:
            print(letter)
        elif counter != 1:
            print(letter + str(counter))
        k += counter

    # encrypted_str = None
    # return encrypted_str


def square_dict(input_dict):
    """
    Сгенерировать dict() из списка ключей ниже по формуле (key : key*key).
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
    """
    d1 = {x: x**2 for x in range(1, 11)}

    return d1

    # squared_dict = None
    # return squared_dict


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    values_list = []
    for i in range(200):
        x = randint(1, 100)
        if x % 2 == 0:
            values_list.append(x)
    return values_list
    # even_int_list = None
    # return even_int_list


def replace_vowels(input_str):
    """
    Заменить в произвольной строке согласные буквы на гласные.
    """
    # гласные
    list_vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    # согласные
    list_consonantal = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч',
                        'ш', 'щ']
    list_out = list(input_str)
    for i in range(len(list_out)):
        for j in range(len(list_vowel)):
            if list_out[i] == list_vowel[j] or list_out[i] == list_vowel[j].upper():
                list_out[i] = list_consonantal[randint(1, len(list_consonantal) - 1)]
    input_str = ''.join(list_out)
    print(input_str)

    # result_str = None
    # return result_str


def filter_unique_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """
    counter = 0
    while True:
        for i in range(len(input_list)):
            for j in range(len(input_list)):
                if input_list[i] == input_list[j]:
                    input_list[j] = randint(1, 100)
                    counter += 1
            counter = 0
        if counter == 0:
            print(input_list)
            break

    # unique_int_list = None
    # return unique_int_list


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    quick_sort(input_list)
    for i in range(-1, -4, -1):
        print(input_list[i])

    # biggest_ints = None
    # return biggest_ints


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    index_min = 1000
    index = 0
    for i in range(len(input_list)):
        if index_min > input_list[i]:
            index_min = input_list[i]
            index = i
    print(index_min, ' - ', index)

    # lowest_int_index = None
    # return lowest_int_index


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    input_list.reverse()
    return input_list

    # reversed = None
    # return reversed


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

    # common_keys = None
    # return common_keys


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
    # your code here
    sorted_dict = None
    return sorted_dict
