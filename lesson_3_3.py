#   Самостоятельная работа по уроку "Произвольное число параметров и HTML_DOM"

import math


#   функция с произвольным числом параметров разного типа
def test_function(txt, *params, slogan="Раз, два, три..", **kwargs):
    print(txt)
    print(params)
    print(slogan)
    print(kwargs)


test_function("Тестовая функция", 1, 2, 3, 4, 5, slogan="Четыре, пять!..", a=1, b=2, c=3, d=4)


#   рекурсивная функция
#   факториал n! = n * (n-1) * (n-2) * ... * 1

def test_factorial(n):
    if n == 1:
        return 1
    else:
        return test_factorial(n - 1) * n


print("Факториал рассчитанный рекурсивной функцией : ", test_factorial(5), "- для n = 5")

#   с помощью модуля math
print("Факториал рассчитанный с помощью модуля math : ", math.factorial(5), "- для n = 5")
