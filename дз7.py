class Matrix:
    def __init__(self, lines):
        self.lines = lines

    def clean(self):
        for i, row in enumerate(self.lines):
            for num in row:
                print(num, end=' ')
            print()
        print('\n')

l1 = [[1,2,3], [2,3,4,], [4,5,6]]
l2 = [[1,2,3], [4,3,2,], [4,6,1]]

m1 = Matrix(l1)
m2 = Matrix(l2)

m1.clean()
m2.clean()