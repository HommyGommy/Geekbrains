# Task 1

from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = {'red': 5, 'yellow': 3, 'green': 1}

    def running(self):
        for color in self.__color:
            print(color)
            sleep(self.__color.get(color))

light = TrafficLight()
light.running()

# Task 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        result = self._length * self._width * 25 * 4
        print(result)

road = Road(30, 40)
road.calc()

# Task 3

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):

    def getfullname(self):
        print(self.name, self.surname, self.position)

    def getincome(self):
        print(self._income_wage + self._income_bonus)

man = Position('Alex', 'Antoshin', 'Manager', {'wage': 5000, 'bonus': 20000})
man.getfullname()
man.getincome()

# Task 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('moving')

    def stop(self):
        print('the car stopped')

    def turn(self, direction):
        print('the car turned', direction)

    def show_speed(self):
        print('the speed is', self.speed)

class TownCar(Car):
    def show_speed(self):
        print('the speed is', self.speed)
        if self.speed > 60:
            print('you are exeeding the speed limit')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('the speed is', self.speed)
        if self.speed > 40:
            print('you are exeeding the speed limit')

class PoliceCar(Car):
    pass

town = TownCar(70, 'white,', 'Hundai', False)
sport = SportCar(100, 'red,', 'BMW', False)
work = WorkCar(30, 'green,', 'Ford', False)
police = PoliceCar(70, 'blue,', 'Chevrolet', True)

town.show_speed()
sport.show_speed()
work.show_speed()
police.show_speed()

# Task 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручки')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандаша')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркера')

pen = Pen('Spider man')
pencil = Pencil('batman')
handle = Handle('boogieman')

pen.draw()
pencil.draw()
handle.draw()