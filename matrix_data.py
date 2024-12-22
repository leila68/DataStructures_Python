class Matrix:
    def __init__(self, mtx):
        self.mtx = mtx

    def matrix_dim(self, mtx=None):
        if mtx is None:
            mtx = self.mtx

        row = len(mtx)
        col = len(mtx[0])
        return row, col

    def display(self, mtx=None):
        if mtx is None:
            mtx = self.mtx
        for row in mtx:
            print(' '.join(map(str, row)))
        print()  # Add a blank line for better readability.

    def matrix_transpose(self):
        row, col = self.matrix_dim()
        # Use list comprehension to transpose the matrix
        transposed = [[self.mtx[i][j] for i in range(row)] for j in range(col)]
        return transposed


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    mt = Matrix(matrix)
    print("Matrix Dimensions:", mt.matrix_dim())
    print("Original Matrix:")
    mt.display()

    print("Transposed Matrix:")
    transposed = mt.matrix_transpose()
    print("Matrix Dimensions:", mt.matrix_dim(transposed))
    mt.display(transposed)
