class Matrix:
    def __init__(self, matrix: list = [[1, 2], [3, 4]]):
        self.matrix = matrix

    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):
        rows = len(self.matrix)
        col = len(self.matrix[0])
        for i in range(rows):
            for j in range(col):
                self.matrix[i][j] += other[i][j]
        return Matrix(self.matrix)

    def __str__(self):
        result = ""
        for rows in self.matrix:
            result += " ".join(list(map(str, rows)))
            result += "\n"
        return f"Матрица следующего вида:\n{result}"


test_1 = Matrix()
test_2 = Matrix()
print(test_1, test_2)
print(test_1 + test_2)