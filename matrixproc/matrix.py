import random


class Operations:
    def __init__(self):
        self.coord_1 = list(input('enter first matrix size\n'))
        self.matrix1 = []
        self.matrix2 = []
        self.size1 = int(self.coord_1[0])
        self.size2 = int(self.coord_1[1])
        for i in range(0, int(self.size1)):
            self.matrix1.append([])
            for b in range(0, int(self.size2)):
                self.matrix1[i].append(int(random.choice(range(0, 20))))
        # self.matrix1, self.size1, self.size2 = a
        # self.matrix2, self.size3, self.size4 = b
        self.new_matrix = []

    def summarizing(self):
        self.coord2 = list(input('enter second matrix size\n'))
        self.matrix2 = []
        self.size3 = int(self.coord2[0])
        self.size4 = int(self.coord2[1])
        for i in range(0, int(self.size3)):
            self.matrix2.append([])
            for b in range(0, int(self.size4)):
                self.matrix2[i].append(int(random.choice(range(0, 20))))
        self.new_matrix = []
        print("Your first matrix is:")
        for b in self.matrix1:
            print(b)
        print('Your second matrix is:')
        for b in self.matrix2:
            print(b)
        if self.size1 == self.size3:
            if self.size2 == self.size4:
                for i in range(0, int(self.size1)):
                    self.new_matrix.append([])
                    for b in range(0, int(self.size2)):
                        self.new_matrix[i].append(self.matrix1[i][b] + self.matrix2[i][b])
                print('Here is your new matrix:')
                for b in self.new_matrix:
                    print(b)
            else:
                print('wrong input')
        else:
            print('wrong input')

    def constant_multiplier(self):
        self.new_matrix = []
        print("Your first matrix is:")
        for b in self.matrix1:
            print(b)
        const = int(input('input your constant:'))
        for i in range(0, int(self.size1)):
            self.new_matrix.append([])
            for b in range(0, int(self.size2)):
                self.new_matrix[i].append(self.matrix1[i][b] * const)
        print('Here is your new matrix:')
        for b in self.new_matrix:
            print(b)

    def matrix_multiplier(self):
        self.coord2 = list(input('enter second matrix size\n'))
        self.new_matrix = []
        self.size3 = int(self.coord2[0])
        self.size4 = int(self.coord2[1])
        for i in range(0, int(self.size3)):
            self.matrix2.append([])
            for b in range(0, int(self.size4)):
                self.matrix2[i].append(int(random.choice(range(0, 20))))

        if self.size2 == self.size3:
            for i in range(self.size1):
                self.new_matrix.append([])
                for k in range(self.size4):
                    self.new_matrix[i].append(0)
            for i in range(0, self.size1):
                for b in range(self.size4):
                    for h in range(self.size2):
                        self.new_matrix[i][b] += int(self.matrix1[i][h]) * int(self.matrix2[h][b])

    def printing(self):
        print("Your first matrix is:")
        for b in self.matrix1:
            print(b)
        print("Your second matrix is:")
        for b in self.matrix2:
            print(b)
        print("Your new matrix is:")
        for b in self.new_matrix:
            print(b)

operator = Operations()

operator.matrix_multiplier()
operator.printing()








