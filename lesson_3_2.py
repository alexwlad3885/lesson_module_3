#   Домашнее задание по уроку "Распаковка параметров и параметры функции"

#   Функция с параметрами по умолчанию
def print_params(a=1, b="строка", c=True):
    print(a, b, c)

#   вызов функции без аргументов
print_params()
#   вызов функции с аргументом "a", остальные по умолчанию
print_params(5)
#   вызов функции с аргументом "a" и "b", а "c" по умолчанию
print_params(6, "линия")
print_params(6, b="линия")
#   вызов функции со всеми аргументами
print_params(15, "зигзаг", False)
print_params(15, b="зигзаг", c=False)
print_params(15, "зигзаг", c=False)

#   предложенные для проверки вызовы функции работают,\
#   но передаваемые значения не соответствует по типу
print_params(b=25)
print_params(c=[1, 2, 3])

#   Распаковка параметров

values_list = [15, "зигзаг", False]
values_dict = {'a': 34, 'b': "элемент", 'c': False}
print_params(*values_list)
print_params(**values_dict)

#   Распаковка + отдельные параметры

values_list_2 = [32, False]
#   предложенный для проверки вызов функции работает
print_params(*values_list_2, 42)
