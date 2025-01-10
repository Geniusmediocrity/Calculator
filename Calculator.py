# Основные модули которые используются в данном приложении
import tkinter as tk
import math
from tkinter import messagebox # Нужен в основном для сообщения пользователю об ошибке


#! Функции:
# Математичесские операции
def insert_sqrt():
    """ Вычисляет квадартный корень выражения """
    try:
        total = math.sqrt(int(calc.get()))
        calc['state'] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0,f'{total}')
        calc['state'] = tk.DISABLED
    except ValueError:
        messagebox.showerror('ValueError', 'При данном значении операция не возможна')
        calc['state'] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0, '0')
        calc['state'] = tk.DISABLED

def insert_square():
    """ Возводит выражение в квадрат """
    value = calc.get()
    if '**' not in value and value[-1] not in '+-*/':
        value = calc.get() + '**'
    else:
        value = value.replace('**', '')
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED

def insert_persentage():
    """ Высчитывает процент выражения от единицы(1/{выражение}) """
    try:
        total = 1 / int(calc.get())
        calc['state'] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0,f'{total}')
        calc['state'] = tk.DISABLED
    except ValueError:
        messagebox.showerror('ValueError', 'При данном значении операция не возможна')
        calc['state'] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0, '0')
        calc['state'] = tk.DISABLED
    except ZeroDivisionError:
        messagebox.showerror('ZeroDivisionError', 'Деление на ноль запрещенно')
        calc['state'] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0, '0')
        calc['state'] = tk.DISABLED
        
def percentage_number():
    """ Переводит выражение в процент """
    try:
        take = int(calc.get())
        total = take * 0.01
        calc['state'] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0, total)
        calc['state'] = tk.DISABLED
    except ValueError:
        messagebox.showerror('ValueError', 'При данном значении операция не возможна')
        calc['state'] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0, '0')
        calc['state'] = tk.DISABLED
        
def un_minus():
    """ Функция задает унарный минус перед значением """    # TODO:!WARNING!!!!!!!!!!!!!!!!!БАГИ!!!!!!!!!!!!!!!!!!!!БАГИ!!!!!!!!!!!!!!!!!!!!!БАГИ!!!!!!!!!!!!!!!!!!!!БАГИ!!!!!!
    value = calc.get() # полученной значение = value
    operations = '-+/*'
    for el in operations: # перебор
        if el in value: # если знак операции встречается в полученном значении(value)...
            index = value.index(el) # индекс знака операции
            if el == '-': # если знак операции "-"...
                if index == 0 and '-' in value[1:]:
                    index = value[1:].index(el)
                    value = value[:index] + value[index:].replace('-', '+')
                elif index != 0:
                    value = value[: index] + value[index:].replace('-', '+') # то заменим знак "-" на знак "+"
                else :
                    value = value[: index] + value[index:].replace('-', '') # убераем его
                if '(' in value or ')' in value:
                    value = value.replace('(', '')
                    value = value.replace(')', '')
                break
            under_processing = value[index + 1:] # значение после знака операции(пускай будет up)
            value = value[:index + 1] # значение перед знаком операции ВКЛЮЧИТЕЛЬНО
            if '-' not in under_processing: # если данное значение(up) НЕ содержит минус, то....
                if el == '+':
                    under_processing = under_processing.replace('+', '-')
                else:
                    under_processing = '(-' + under_processing + ')'
                value += under_processing # добавляем его
            else: # если данное значение(up) содержит унарный минус, то....
                new_processing = ''
                for el in under_processing:
                    if el.isdigit():
                        new_processing += el
                under_processing = new_processing
                value += under_processing # убераем этот унарный минус из значения
            break #  прерываем цикл чтобы не выполнялся блок else

    else: # если знак операции НЕ встречается в полученном значении(value)...
        # то => данное значение(value) НЕ содержит унарный минус, то....
        value = '-' + value # добавляем его

    calc.delete(0, tk.END)
    calc.insert(0, value)
    
# Операции удаления значения
def delete_last():
    """ Удаляет последний элемент в выражении в виджете Entry """
    value = calc.get()
    value = value[:-1]
    if len(value) == 0:
        value = 0
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED

def delete_all():
    """ Удалаяет все выражение в виджете Entry """
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED

# Вычисление значения
def calculate():
    """ Считает значение которое находится в виджете Entry(которое задал пользователь) """
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showerror('ZeroDivisionError', 'Деление на ноль запрещенно')
        calc.insert(0, '0')
    except ValueError:
        messagebox.showerror('ValueError', 'При данном значении операция не возможна')
        calc.insert(0, '0') 
    calc['state'] = tk.DISABLED

# Создание кнопок
def make_digit_button(digit):
    """ Создает кнопки цифр

    Args:
        digit (_str_): цифра кнопка которой будет создана
    Returns:
        _Button_: возвращает кнопку в окне win
    """
    return tk.Button(win, text=digit, bg='#000000', fg='white', bd=1, font=('Arial', 13), command=lambda: add_digit(digit))

def make_operation_button(operation):
    """ Создает кнопки математичесских операций

    Args:
        operation (_str_): математичесская операция кнопка которой будет создана
    Returns:
        _Button_: возвращает кнопку в окне win
    """
    return tk.Button(win, text=operation, bg='#f27e30', fg='white', bd=1, font=('Arial', 13), command=lambda: add_operation_button(operation))

# Печать значения кнопок
def add_operation_button(operation):
    """ Печатает значения математических операций

    Args:
        operation (_str_): математичесская операция которая находилась в кнопке
    """
    value = calc.get()
    if value[-1] in '+=-/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)
    calc['state'] = tk.DISABLED

def add_digit(digit):
    """ Печатает цифру которая находилась в кнопке

    Args:
        digit (_str_): цифра которая находилась в кнопке
    """
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)
    calc['state'] = tk.DISABLED

def press_key(event):
    """ Эта функция берет значения с клавиатуры и добавляет его в поле ввода Entry

    Args:
        event (_str_): значение получаемое с клавиатуры
    """
    char = event.char
    calc['state'] = tk.NORMAL
    if char.isdigit():
        add_digit(char)
    elif char in '-+/*':
        add_operation_button(char)
    elif char == '\r' or char == '=': # это клавиша Enter(данное значение получено при помощи функции repr() )
        calculate()
    elif char == '\x08': # это клавиша Backspace(данное значение получено при помощи функции repr() )
        delete_last()
    calc['state'] = tk.DISABLED




#! Окно:
win = tk.Tk() # Само окно
win.geometry('320x525+50+100') # Размеры
win.title('Калькулятор') # Имя окна
win['bg'] ='#A5A3A3' # Цвет фона
# Иконка приложения:
icon = tk.PhotoImage(file='icons8-calculator-50.png')
win.iconphoto(False, icon)
# Бинд ввода с клавиатуры
win.bind('<Key>', press_key)


#! Виджеты Ввода(Entry):
""" Виджет Ввода(Entry) """
calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 20, 'bold'))
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4,  stick='wens')


#! Виджеты кнопки(Button):
""" Виджеты кнопки(Button) выполняющие какие-либо взаимодействия с выражением """
tk.Button(win, text='%', bg='#ffe600', fg='black', bd=1, font=('Arial', 13), command=percentage_number).grid(row=1, column=0, stick='wens')
tk.Button(win, text='+/-', bg='#ffe600', fg='black', bd=1, font=('Arial', 13), command=un_minus).grid(row=1, column=1, stick='wens')
tk.Button(win, text='C', bg='#ffe600', fg='black', bd=1, font=('Arial', 13), command=delete_all).grid(row=1, column=2, stick='wens')
tk.Button(win, text='⌫', bg='#ffe600', fg='black', bd=1, font=('Arial', 13), command=delete_last).grid(row=1, column=3, stick='wens')
tk.Button(win, text='1/x', bg='#ffe600', fg='black', bd=1, font=('Arial', 13), command=insert_persentage).grid(row=2, column=0, stick='wens')
tk.Button(win, text='xⁿ', bg='#ffe600', fg='black', bd=1, font=('Arial', 13), command=insert_square).grid(row=2, column=1, stick='wens')
tk.Button(win, text='√', bg='#ffe600', fg='black', bd=1, font=('Arial', 13), command=insert_sqrt).grid(row=2, column=2, stick='wens')

""" Виджеты кнопки(Button) цифры + их функциональное использование """
make_digit_button('1').grid(row=3, column=0, stick='wens')
make_digit_button('2').grid(row=3, column=1, stick='wens')
make_digit_button('3').grid(row=3, column=2, stick='wens')
make_digit_button('4').grid(row=4, column=0, stick='wens')
make_digit_button('5').grid(row=4, column=1, stick='wens')
make_digit_button('6').grid(row=4, column=2, stick='wens')
make_digit_button('7').grid(row=5, column=0, stick='wens')
make_digit_button('8').grid(row=5, column=1, stick='wens')
make_digit_button('9').grid(row=5, column=2, stick='wens')
make_digit_button('0').grid(row=6, column=0, columnspan=2, stick='wens')

""" Виджеты кнопки(Button) цифры + их функциональное использование """
make_operation_button('/').grid(row=2, column=3, stick='wens')
make_operation_button('*').grid(row=3, column=3, stick='wens')
make_operation_button('-').grid(row=4, column=3, stick='wens')
make_operation_button('+').grid(row=5, column=3, stick='wens')
make_digit_button('.').grid(row=6, column=2, stick='wens')

""" Виджеты кнопки(Button) которая высчитывает выражение для получение ответа """
tk.Button(win, text='=', bg='#f27e30', fg='white', bd=1, font=('Arial', 13), command=calculate).grid(row=6, column=3, stick='wens')


#! Настройки метода грид, атрибута КОЛОНА(column)
win.grid_columnconfigure(index=0, minsize=80)
win.grid_columnconfigure(index=1, minsize=80)
win.grid_columnconfigure(index=2, minsize=80)
win.grid_columnconfigure(index=3, minsize=80)

#! Настройки метода грид, атрибута РЯД(row)
win.grid_rowconfigure(index=0, minsize=75)
win.grid_rowconfigure(index=1, minsize=75)
win.grid_rowconfigure(index=2, minsize=75)
win.grid_rowconfigure(index=3, minsize=75)
win.grid_rowconfigure(index=4, minsize=75)
win.grid_rowconfigure(index=5, minsize=75)
win.grid_rowconfigure(index=6, minsize=75)

win.mainloop() # Основной цикл окна