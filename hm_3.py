# task 1

def divison():

    first_num = int(input('enter the first number: '))
    second_num = int(input('enter the second number: '))
    try:
        return first_num/second_num
    except ZeroDivisionError:
        print('you are trying to divide by 0')
        return ''

print(divison())

# task 2

def info():
    name = str(input('enter your name: ')).capitalize()
    surname = str(input('enter your surname: ')).capitalize()
    yob = input('enter your year of birth in YYYY format: ')
    city = str(input('enter your city of residence: ')).capitalize()
    email = str(input('enter your email: '))
    phone = input('enter your phone number: ')
    print(name, surname, yob, city, email, phone)

info()

# task 3

def my_func(a,b,c):
    sum_list = []
    first_list = [a,b,c]

    sum_list.append(max(first_list))
    first_list.remove(max(first_list))
    sum_list.append(max(first_list))
    return sum(sum_list)

result = my_func(3,4,5)
print(result)

# task 4 (with * )

def pow_func(x,y):
    print(x ** y)
pow_func(3,3)

# task 4 (with recursion )

def pow_func(x,y):
    if y == 0:
        return 1
    if y == 1:
        return x
    return x * pow_func(x, y - 1)

print(pow_func(3,5))

# task 5

from itertools import chain

def conti_sum():
    str_list = []
    int_list = []
    stop_sign = 'stop'
    user_input = str(input('enter a new num or type stop to end: '))
    str_list.append(user_input.split())
    str_list_chain = list(chain.from_iterable(str_list))
    # здесь оборачиваю строку, которую вводит юзер в список, разделяя пробелом

    def is_int(some_int):
        """  функция нужна, чтобы итерироваться по списку str_list_chain и проверять тип каждого элемента;
             если float (int так же преобразовывается в float), возвращает True, на все остальное False
        """
        try:
            float(some_int)
        except ValueError:
            return False
        else:
            return type(float(some_int)) == float

    if stop_sign in str_list_chain:
        str_list_chain = str_list_chain[:str_list_chain.index(stop_sign)]
        for i in str_list_chain:
            if is_int(i) == True:
                int_list.append(float(i))
            else:
                pass
        return sum(int_list)
    # проверяю есть ли стоп-символ в строк:
    # - если есть, то отсекаю список до стоп-символа, проверяю на тип и уже int/float
    #   добавляю в новый список int_list суммирую его
    else:
        for i in str_list_chain:
            if is_int(i) == True:
                int_list.append(float(i))
            else:
                pass
    return sum(int_list) + conti_sum()
   # - если стоп-символа нет, int/float добавляю в int_list, суммирую его и через рекурсию вызываю функцию заново

print('sum of your numbers =', conti_sum())

# task 6

def int_func():
    snake_str = input('enter text: ')
    return snake_str.lower().title()

print(int_func())