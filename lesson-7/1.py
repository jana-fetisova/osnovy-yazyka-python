a = [[2, 4, 6, 7], [1, 8, 9, 6], [2, 9, 7, 5]]
b = [[3, 9, 4, 1], [3, 4, 5, 9], [2, 2, 2, 1]]

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))

matrix1 = Matrix(a)
matrix2 = Matrix(b)

print(matrix1, '\n')
print(matrix2, '\n')
print(matrix1 + matrix2)
