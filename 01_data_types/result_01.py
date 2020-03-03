
def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    return [i for i in url_list if '/catalog/' in i]


def idiotic_str(input_str):
    """
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """
    idiotic_str = ''
    for i in input_str:
        idiotic_str += i.upper() if len(idiotic_str) % 2 else i
    return idiotic_str


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    point = len(input_str) // 2
    output_str = input_str[point - 1: 1 - point]
    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    output_dict = dict()
    for i in input_str:
        output_dict.update({i: output_dict.get(i, 0) + 1})
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    return str1[:(len(str1) // 2)] + str2 + str1[(len(str1) // 2):]


def avg_score(score_list):
    """
    Дописать функцию, которая принимает список строк с оценками, а возвращает
    список строк со средним баллом
    Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
    ["Mike|65", "Jane|42"]
    """
    avg_scores = list()
    for student in score_list:
        name, str_scores = student.split('|')
        scores_list = str_scores.split(', ')
        scores = [int(score) for score in scores_list]
        avg_score = f'{name}|{sum(scores) // len(scores)}'
        avg_scores.append(avg_score)
    return avg_scores


def square_dict(input_list):
    """
    Сгенерировать dict() из списка ключей ниже по формуле (key : key*key).
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
    """
    return {number: number*number for number in input_list}


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    return [i for i in range(0, 101, 2)]


def replace_vowels(input_str):
    """
    Заменить в произвольной строке согласные буквы на гласные.
    """
    import random
    vowels = ["a", "e", "i", "o", "u"]
    output = list(input_str)
    for index, letter in enumerate(input_str):
        if letter.lower() not in vowels and letter.lower() != " ":
            output[index] = random.choice(vowels)
    return "".join(output)


def filter_unique_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """
    return list(set(input_list))


def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    return sorted(set(input_list))[-3:]


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    return input_list.index(min(input_list))


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    return list(reversed(input_list))


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    return list(set(dict1.keys()) & set(dict2.keys()))
