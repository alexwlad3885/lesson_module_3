"""Домашняя работа по уроку 'Пространство имён'"""


calls = 0


def count_calls(n):
    global calls
    calls += n
    return calls


def string_info(string: str):
    count_calls(1)
    res_tuple = ()
    str_len = len(string)
    str_up = string.upper()
    str_low = string.lower()
    res_tuple = (str_len, str_up, str_low)
    return res_tuple


def is_contains(string, list_to_search):
    count_calls(1)
    list_to_search_ = []
    for i in list_to_search:
        elem = i.lower()
        list_to_search_.append(elem)
    if string.lower() in list_to_search_:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
