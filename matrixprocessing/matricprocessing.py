import random


class Matrix:

    def __init__(self, rows, columns, matrix: list):
        self.rows = rows
        self.columns = columns
        self.matrix = []
        self.matrix_starter_list = matrix

    def matrix_formatizer(self) -> list:
        """turns list of numbers into structured nested lists"""
        counter = 0
        for i in range(0, self.rows):
            self.matrix.append([])
            for b in range(0, self.columns):
                self.matrix[i].append(int(self.matrix_starter_list[counter]))
                counter += 1
        return self.matrix

    def const_multipl(self, number: int) -> list:
        self.matrix = self.matrix_formatizer()
        result_matrix = []
        for i in range(0, self.rows):
            result_matrix.append([])
            for b in range(0, self.columns):
                result_matrix[i].append(int(self.matrix[i][b]) * int(number))
        return result_matrix

    def matrix_multipl(self, other) -> list or str:
        """multiplying one matrix by another"""
        if self.columns != other.rows:
            return 'these matrices can`t be multiplied'
        else:
            self.matrix = self.matrix_formatizer()
            other.matrix_formatizer()
            result = [[0] * other.columns for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(other.rows):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return result

    def __add__(self, other) -> list or str:
        if self.rows != other.rows or self.columns != other.columns:
            return "Matrices aren't the same size"
        else:
            self.matrix = self.matrix_formatizer()
            other_matrix = Matrix(other.rows, other.columns, other.matrix_starter_list)
            other_matrix.matrix_formatizer()
            result_matrix = []
            for i in range(0, self.rows):
                result_matrix.append([])
                for b in range(0, self.columns):
                    result_matrix[i].append(int(self.matrix[i][b]) + int(other_matrix.matrix[i][b]))
            return result_matrix

    def transpose_main(self) -> list:
        """transposing matrix by main diagonal"""
        result = [[0] * self.rows for _ in range(self.columns)]
        for i in range(self.rows):
            for b in range(self.columns):
                result[b][i] += self.matrix[i][b]
        return result

    def transpose_secondary(self) -> list or str:
        """transposing matrix by secondary diagonal"""
        if self.rows != self.columns:
            return 'this operation can only be performed with a square matrix'
        else:
            self.matrix = self.matrix_formatizer()
            result = [[0] * self.rows for _ in range(self.columns)]
            for i in range(self.rows):
                for b in range(self.rows):
                    result[self.rows-i-1][self.rows-b-1] += self.matrix[i][b]
            return result

    def transpose_vertical(self) -> list or str:
        """transposing matrix by vertical"""
        if self.rows != self.columns:
            return 'this operation can only be performed with a square matrix'
        else:
            self.matrix = self.matrix_formatizer()
            result = [[0] * self.columns for _ in range(self.rows)]
            for i in range(self.rows):
                for b in range(self.rows):
                    result[i][self.rows-b-1] += self.matrix[i][b]
            return result

    def transpose_horizontal(self) -> list or str:
        """transposing matrix by vertical"""
        if self.rows != self.columns:
            return 'this operation can only be performed with a square matrix'
        else:
            self.matrix = self.matrix_formatizer()
            result = [[] for _ in range(self.columns)]
            for i in range(self.rows):
                for b in range(self.rows):
                    result[-i - 1] = self.matrix[i]
            return result

    def matrix_minor(self, matrix, i, j):
        """Calculates the minor of a matrix"""
        minor = []
        if len(matrix) == 1:
            return matrix[0][0]
        else:
            for row_idx in range(len(matrix)):
                if row_idx == i:
                    continue
                current_row = []
                for col_idx in range(len(matrix[row_idx])):
                    if col_idx == j:
                        continue
                    current_row.append(matrix[row_idx][col_idx])
                minor.append(current_row)
            return self.determinant(minor)

    def determinant(self, matr):
        """Calculates the determinant of a square matrix"""
        n = len(matr)
        if n == 1:
            return matr[0][0]
        elif n == 2:
            return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
        else:
            det = 0
            for j in range(n):
                sign = (-1) ** j
                minor = self.matrix_minor(matr, 0, j)
                det += sign * matr[0][j] * minor
            return det

    def invertible(self):
        """creates inverted matrix"""
        self.matrix = self.matrix_formatizer()
        det = int(self.determinant(self.matrix))
<<<<<<< HEAD
        if det == 0:
            return 'this matrix can`t be inverted'
        else:
            n = len(self.matrix)
            result = [[0] * n for _ in range(n)]
            soyuz = [[0] * n for _ in range(n)]
            for j in range(n):
                for k in range(n):
                    sign = (-1) ** (j + k)
                    minor = self.matrix_minor(self.matrix, j, k)
                    soyuz[j][k] += sign * minor
            soyuz = Matrix(n, n, soyuz)
            soyuz.matrix = soyuz.matrix_starter_list
            soyuz = soyuz.transpose_main()
            for i in range(n):
                for b in range(n):
                    result[i][b] += (soyuz[i][b] / det)
            return result
=======
        # if det == 0:
        #     return 'this matrix can`t be inverted'
        # else:
        n = len(self.matrix)
        result = [[0] * n for _ in range(n)]
        soyuz = [[0] * n for _ in range(n)]
        for j in range(n):
            for k in range(n):
                sign = (-1) ** (j + k)
                minor = self.matrix_minor(self.matrix, j, k)
                soyuz[j][k] += sign * minor
        soyuz = Matrix(n, n, soyuz)
        soyuz.matrix = soyuz.matrix_starter_list
        soyuz = soyuz.transpose_main()
        for i in range(n):
            for b in range(n):
                result[i][b] += (soyuz[i][b] / det)
        return result
>>>>>>> 22158ca7d9aedc250a1acd93ddaaa21440550231

def correct_input(a, b, c) -> bool:
    """checking if matrix input is correct"""
    if (a*b) != c:
        return True
    else:
        return False

# 45 56 25 13 7 34 5 6 98


def menu():
    """full-scale meny for matrix calculator"""
    first_rows_columns = input('input numbers of rows and columns: ')
    first_matrix = input('input your matrix: ').split()
    if correct_input(int(first_rows_columns.split()[0]),
                     int(first_rows_columns.split()[1]), len(first_matrix)):
        print('Number of elements in your matrix is incorrect')
    else:
        operation = input('choose your operation:\n write "1" to sum\n'
                          ' "2" multiply by constant\n'
                          ' "3" to multiply two matrices on each other\n '
                          ' "4" to transpose \n'
                          ' "5" to calculate a determinant\n'
                          ' "6" to calculate inverted matrix')
        if operation == '1':
            second_rows_columns = input('input numbers of rows and columns: ')
            second_matrix = input('input your matrix: ').split()
            if correct_input(int(second_rows_columns.split()[0]),
                     int(second_rows_columns.split()[1]), len(second_matrix)):
                print('Number of elements in your matrix is incorrect')
            else:
                matrix_one = Matrix(int(first_rows_columns.split()[0]),
                                    int(first_rows_columns.split()[1]), first_matrix)
                matrix_two = Matrix(int(second_rows_columns.split()[0]),
                                    int(second_rows_columns.split()[1]), second_matrix)
                print(matrix_one + matrix_two)

        elif operation == '2':
            number = int(input('input multiplier: '))
            matrix_one = Matrix(int(first_rows_columns.split()[0]),
                                int(first_rows_columns.split()[1]), first_matrix)
            print(matrix_one.const_multipl(number))

        elif operation == '3':
            second_rows_columns = input('input numbers of rows and columns')
            second_matrix = input('input your matrix').split()
            if (correct_input(second_rows_columns.split()[0], int(second_rows_columns.split()[1]),
                              len(second_matrix))):
                print('Number of elements in your matrix is incorrect')
            else:
                matrix_one = Matrix(int(first_rows_columns.split()[0]),
                                    int(first_rows_columns.split()[1]), first_matrix)
                matrix_two = Matrix(int(second_rows_columns.split()[0]),
                                    int(second_rows_columns.split()[1]), second_matrix)
                print(matrix_one.matrix_multipl(matrix_two))

        elif operation == "4":
            operation = int(input('what kind of transposition you wnat yo happen here?'
                                  '\n 1.By main diagonal'
                                  '\n 2.By secondary diagonal'
                                  '\n 3.By vertical'
                                  '\n 4.By horizontal '))
            matrix_one = Matrix(int(first_rows_columns.split()[0]),
                                int(first_rows_columns.split()[1]), first_matrix)
            match operation:
                case 1:
                    matrix_one.matrix = matrix_one.matrix_formatizer()
                    result = matrix_one.transpose_main()
                case 2:
                    result = matrix_one.transpose_secondary()
                case 3:
                    result = matrix_one.transpose_vertical()
                case 4:
                    result = matrix_one.transpose_horizontal()
            print(result)

        elif operation == "5":
            matrix_one = Matrix(int(first_rows_columns.split()[0]),
                                int(first_rows_columns.split()[1]), first_matrix)
            matrix_one = Matrix(int(first_rows_columns.split()[0]),
                                int(first_rows_columns.split()[1]), matrix_one.matrix_formatizer())
            matrix_one.matrix = matrix_one.matrix_starter_list
            result = matrix_one.determinant(matrix_one.matrix)
            print(result)

        elif operation == "6":
            matrix_one = Matrix(int(first_rows_columns.split()[0]),
                                int(first_rows_columns.split()[1]), first_matrix)
            result = matrix_one.invertible()
            print(result)


answer= 'y'
while answer == 'y':
    menu()
    answer = input('would you like to start over?y/n ')
print('program is over')
