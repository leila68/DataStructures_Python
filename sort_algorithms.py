class Search:
    def __init__(self, data):
        self.data = data
        self.size = len(self.data)

    def binary_search(self, val):
        left, right = 0, self.size - 1

        while left <= right:
            mid = (left + right) // 2
            if val == data[mid]:
                return data[mid]
            if val < data[mid]:
                right = mid - 1
            if val > data[mid]:
                left = mid + 1
        return 0

    def bubble_sort(self):
        for i in range(self.size-1):
            for j in range(self.size-1-i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return data


if __name__ == '__main__':
    # data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    data = [100, 60, 40, 70, 50, 20, 80, 90, 10]
    sr = Search(data)
    print(sr.bubble_sort())
    print(sr.binary_search(90))




