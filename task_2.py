def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    dict_ = {}
    str_ = ''.join(str_.lower())
    for value in str_:
        if value.isalpha():
            if value in dict_:
                dict_[value] += 1
            else:
                dict_[value] = 1
    return dict_

def percent_char(count_char_dict):
    i = 0
    percent_dict = {}
    for char in count_char_dict:
        i += count_char_dict.get(char) #общее количество букв
    #print(i)
    for char in count_char_dict:
        percent_dict[char] = round((count_char_dict.get(char)/i)*100, 2)
    #проверка, что сумма процентов равна 100
    check = 0
    for char in percent_dict:
        check += percent_dict.get(char)
    #print(round(check, 1))
    return percent_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
