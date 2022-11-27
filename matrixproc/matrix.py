import random


def second_matrix_maker():
    coord_2 = list(input('enter second matrix size\n'))
    matrix_2 = []
    size_3 = coord_2[0]
    size_4 = coord_2[1]
    for i in range(0, int(size_3)):
        matrix_2.append([])
        for b in range(0, int(size_4)):
            matrix_2[i].append(int(random.choice(range(0, 20))))
    return [matrix_2, size_3, size_4]


def first_matrix_maker():
    coord_1 = list(input('enter first matrix size\n'))
    matrix_1 = []
    size_1 = coord_1[0]
    size_2 = coord_1[1]
    for i in range(0, int(size_1)):
        matrix_1.append([])
        for b in range(0, int(size_2)):
            matrix_1[i].append(int(random.choice(range(0, 20))))
    return [matrix_1, size_1, size_2]


class Operations:
    def __init__(self, a, b):
        self.matrix1, self.size1, self.size2 = a
        self.matrix2, self.size3, self.size4 = b
        self.new_matrix = []

    def summarizing(self):
        print(f"Your first matrix is \n{self.matrix1}")
        print(f'Your second matrix is \n{self.matrix2}')
        if self.size1 == self.size3:
            if self.size2 == self.size4:
                for i in range(0, int(self.size1)):
                    self.new_matrix.append([])
                    for b in range(0, int(self.size2)):
                        self.new_matrix[i].append(self.matrix1[i][b] + self.matrix2[i][b])
                return print(f'Here is your new matrix \n{self.new_matrix}')


operator = Operations(first_matrix_maker(), second_matrix_maker())

operator.summarizing()








