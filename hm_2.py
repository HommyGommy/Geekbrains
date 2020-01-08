# task 1

first_list = [1, 'str', True, 5.4]

for i in first_list:
    print(type(i))

# task 2

init_list = ['a','b','c','d','e','f']
fin_list = init_list

requested_elements = int(input('Укажите число элементов: '))

for i, el in enumerate(fin_list, 1):
    if i % 2 == 0 and i-1 < requested_elements:
        deleted_item = fin_list.pop(i-1)
        fin_list.insert(i-2, deleted_item)

print(fin_list)

# task 3

month_number = int(input('please enter a month number from 1 to 12: '))
seasons = {'winter': [12,1,2], 'spring': [3,4,5], 'summer': [6,7,8], 'fall': [9,10,11]}

for i in seasons:
    if month_number in seasons.get(i):
        print(i)
        break
else:
    print('check month number')

# task 4

new_str = input('please enter a string: ')
listed_str = new_str.split()

for i in listed_str:
    if len(i) > 10:
        print(i[:10])
    elif len(i) <= 10:
        print(i)

# task 5

my_list = [7,5,3,3,2]
new_el = int(input('please enter a number: '))

my_list.append(new_el)
my_list.sort(reverse = True)

print(my_list)

# task 6

name_1 = input('что будет первым? ')
price_1 = input('укажите цену: ')
qty_1 = input('укажите кол-во: ')
meas_1 = input('укажите ед измерения: ')

name_2 = input('что будет вторым?: ')
price_2 = input('укажите цену: ')
qty_2 = input('укажите кол-во: ')
meas_2 = input('укажите ед измерения: ')

name_3 = input('что будет третьим? ')
price_3 = input('укажите цену: ')
qty_3 = input('укажите кол-во: ')
meas_3 = input('укажите ед измерения: ')

last_list = [
(1, {'название': name_1, 'цена': price_1, 'количество': qty_1, 'ед': meas_1}),
(2, {'название': name_2, 'цена': price_2, 'количество': qty_2, 'ед': meas_2}),
(3, {'название': name_3, 'цена': price_3, 'количество': qty_3, 'ед': meas_3})]

fin_dict = {'название': [], 'цена': [], 'количество': [], 'ед': []}
empty_list = []

for tup in last_list:
    empty_list.append(tup[1])

for i in new_list:
    fin_dict['название'].append(i['название'])
    fin_dict['цена'].append(i['цена'])
    fin_dict['количество'].append(i['количество'])
    fin_dict['ед'].append(i['ед'])

fin_dict['ед'] = list(set(fin_dict['ед']))

print(fin_dict)


# homework_1
# task 1

num = 5
float = 5.7
string = 'hello'
bool = True

print(num, float, string, bool)

input_num = input('Укажите число: ')
input_str = input('Укажите  строку: ')
print(input_num, input_str)


# task 2

import time
seconds = input('Введите количество секунд: ')
answer = time.strftime('%H:%M:%S',  time.gmtime(seconds))

print(answer)

# task 3

n = input('Введите число: ')
result = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(result)

# task 4

number = int(input('Введите число: '))
r = -1
while number > 10:
    d = number % 10
    number //= 10
    if d > r:
        r = d
print(r)

# task 5

revenue = int(input('Укажите выручку фирмы: '))
cost = int(input('Укажите издержки фирмы: '))

profit = revenue - cost
loss = cost - revenue

if revenue > cost:
    print('Прибыль фирмы равна', profit)
    print('Рентабельность фирмы равна', round(profit/revenue, 2))
elif revenuew < cost:
    print('Убыток фирмы равен', loss)

employees = input('Сколько сотрудников в фирме? ')
print('Прибыль в расчете на одного сотрудника равна', profit/employees)

# task 6

a = 2
b = 3
counter = 0

while a < b:
    a *= 1.1
    counter += 1
print(int(counter) + 1)