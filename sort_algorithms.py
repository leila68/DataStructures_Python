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


if __name__ == '__main__':
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    sr = Search(data)
    print(sr.binary_search(90))



