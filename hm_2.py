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