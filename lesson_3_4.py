#   программа "Калькулятор"
#   функция принимающая значение
def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

#   функция сложения
def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

#   функция вычитания
def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

#   функция умножения
def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

#   функция деления
def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

import tkinter as tk

window = tk.Tk()                #   создаем графическое окно
window.title('Калькулятор')     #   задаем имя окну
window.geometry("350x350")      # задаем размеры окну
window.resizable(False, False)    # блокируем изменение размеров окна
button_add = tk.Button(window, text="+", width=4, height=2, command=add)
button_add.place(x=50, y=170)
button_sub = tk.Button(window, text="-", width=4, height=2, command=sub)
button_sub.place(x=120, y=170)
button_mul = tk.Button(window, text="*", width=4, height=2, command=mul)
button_mul.place(x=190, y=170)
button_div = tk.Button(window, text="/", width=4, height=2, command=div)
button_div.place(x=260, y=170)
number1_entry = tk.Entry(window, width=41)
number1_entry.place(x=50, y=75)
number2_entry = tk.Entry(window, width=41)
number2_entry.place(x=50, y=120)
answer_entry = tk.Entry(window, width=41)
answer_entry.place(x=50, y=250)
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=50, y=52)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=50, y=97)
answer = tk.Label(window, text="Ответ:")
answer.place(x=50, y=227)

window.mainloop()               #   обновление информации о происходящем на экране