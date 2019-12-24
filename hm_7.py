# Task 1

class Matrix:
    def __init__(self, line):
        self.line = line
        self.sumlist = []

    def clean(self):
        for i, row in enumerate(self.line):
            for num in row:
                print(num, end=' ')
            print()
        print('\n')

    def __add__(self, other):
        return map(sum, other)

l1 = [[1, 2, 3], [1, 2, 5], [1, 3, 6]]
l2 = [[6, 3, 1], [1, 2, 5], [2, 7, 1]]
m1 = Matrix(l1)
m2 = Matrix(l2)
m1.clean()
m2.clean()

l1 + l2
