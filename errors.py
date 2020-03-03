def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    # Нет необходимости объявлять переменную перед ее использованием
    result_str = ''
    # Дерзкая конкатенация плюсами - не всегда хорошая идея. Если нам нужна
    # строка - лучше собирать ее сразу как строку, с помощью f'{}{}{}'
    result_str = str1[:int(len(str1)/2)] + str2 + str1[int(len(str1)/2):]
    # Можно возвращать выражение:
    return result_str

    str_center = len(str1)//2
    return f'{str1[:str_center]}{str2}{str1[str_center:]}'



def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    output_str = ''
    # len(input_str) % 2 возвращает 0 или число, которые можно интерпретировать
    # как False и True соответственно.
    # if len(input_str) % 2: - будет достаточно
    if len(input_str) % 2 == 0:
        # int(len(input_str)/2) - можно избежать кастования результатов в int,
        # если использовать //
        output_str = input_str[(int(len(input_str)/2)-1):(int(len(input_str)/2)+1)]
    else:
        # Избежать длинных сложных однострочников можно вынося их части
        # в переменные.
        # start_i = len(input_str) // 2 - 1
        # end_i = len(input_str) // 2 + 2
        output_str = input_str[(int(len(input_str)/2)-1):(int(len(input_str)/2)+2)]
    return output_str
