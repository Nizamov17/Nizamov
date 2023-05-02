class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(elem) for elem in row) + "\n"
        return matrix_str

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrix dimensions must match!")
        result = []
        for i in range(len(self.data)):
            result.append([])
            for j in range(len(self.data[0])):
                result[i].append(self.data[i][j] + other.data[i][j])
        return Matrix(result)