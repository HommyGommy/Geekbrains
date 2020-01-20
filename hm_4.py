# Taks 1
from sys import argv

rate, hours, bonus = argv
print('Salary = ', float(argv[1]) * float(argv[2]) + int(argv[3]))

# Task 2

some_list = [1, 2, 5, 7, 22, 10]

gen_list = [el for i, el in enumerate(some_list) if some_list[i] > some_list[i-1]]
print(gen_list)

# Taks 3

print([el for el in range(20,40) if el % 20 == 0 or el % 21 == 0])

# Task 4

fourth_list = [44, 11, 5, 67, 12, 6, 3, 3, 104, 44]
fourth_gen = [el for el in fourth_list if fourth_list.count(el) == 1]
print(fourth_gen)

# Task 5
from functools import reduce

def mult_omg(a, b):
    return a * b

gener = [el for el in range(100, 1001) if el % 2 ==0]

print(reduce(mult_omg, gener))

# Task 6

import  itertools
list_new = [1,2, 'abc']
for i in itertools.count(start=int(input('Start number is: ')), step= 1):
    print(i)

for el in itertools.cycle(list_new):
    print(el)

# Task 7

import math

def fibo_gen():
    x = int(input('enter factorial: '))
    for el in itertools.count(1):
        if el > x:
            break
        else:
            yield el

def multi_cont(x, y):
    return x * y

for el in fibo_gen():
    if el < 16:
        print(el)
result = reduce(multi_cont, fibo_gen())
print(result)







