class Matrix:
    def __init__(self, mtx):
        self.mtx = mtx

    def matrix_dim(self):
        row = len(self.mtx)
        col = len(self.mtx[0])

        return row, col

    def display(self):
        row, col = self.matrix_dim()
        for i in range(row):
            for j in range(col):
                print(self.mtx[i][j], end=' ')
            print('')

    def new_matrix_dim(self, mtx):
        row = len(mtx)
        col = len(mtx[0])
        return row, col

    def new_display(self, mtx):
        row, col = self.new_matrix_dim(mtx)
        for i in range(row):
            for j in range(col):
                print(mtx[i][j], end=' ')
            print('')

    def matrix_transpose(self):
        row, col = self.matrix_dim()
        trans_mtx = [[0] * row for _ in range(col)]
        # transposed = []
        # for _ in range(cols):
        #     transposed.append([0] * rows)

        for i in range(row):
            for j in range(col):
                trans_mtx[j][i] = self.mtx[i][j]
        self.new_display(trans_mtx)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    mtx = Matrix(matrix)

    mtx.display()
    print(mtx.matrix_dim())
    mtx.matrix_transpose()


