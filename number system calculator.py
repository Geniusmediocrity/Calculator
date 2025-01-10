from termcolor import colored


def checking_the_result(list_):
    comparative_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P']
    for i in range(len(list_)):
        ind = int(list_[i])
        if comparative_list[ind] not in '0123456789':
            list_[i] = comparative_list[ind]
    return list_


def foolproof(checked_number):
    while not checked_number.isdigit():
        checked_number = input(colored('Введено неверное значение. \nВведите значение снова:  ', 'red'))
    return int(checked_number)


def calc_sys(num, sys):
    output_list = []
    private = 0
    ostatok = 0
    range_sys = [i for i in range(sys)]

    while num not in range_sys:
        private = num // sys # 26
        ostatok = num - (private * sys) # 428 - (16 * 26)
        num = private
        output_list.append(str(ostatok))

    output_list.append(num)
    output_list = output_list[::-1]
    total = checking_the_result(output_list)
    return total

    
number_to_calc = input(colored('Введите число для перевода из 10 системы счисления:  ', 'yellow')) # int
number_to_calc = foolproof(number_to_calc)

numbers_sys = input(colored('Введите систему счисления в которую желаете осуществить перевод:  ', 'yellow')) # int
numbers_sys = foolproof(numbers_sys)

print(colored('result:  ', 'green'), *calc_sys(number_to_calc, numbers_sys), sep='')