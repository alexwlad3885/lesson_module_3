#   Домашнее задание по уроку "Пространство имен и способы вызова функции"

#   Функция с двумя переменными
def test():
    a = 5
    b = 16
    print(a, b)


test()


#   функция с тремя параметрами
def test2(a, b, *, c):
    print(a, b, c)


test2(8, 24, c="Unit")
