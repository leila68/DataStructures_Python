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
        # time complexity: O(n^2)
        for i in range(self.size-1):
            for j in range(self.size-1-i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return data

    def selection_sort(self):
        # time complexity: O(n^2)
        end = self.size-1
        while end >= 0:
            max_idx = 0
            for i in range(end+1):
                if self.data[i] > self.data[max_idx]:
                    max_idx = i
            self.data[max_idx], self.data[end] = self.data[end], self.data[max_idx]
            end -= 1

        return self.data

    def insertion_sort(self):
        # time complexity: O(n^2)
        for i in range(1, self.size):
            key = self.data[i]
            j = i-1
            while j >= 0 and self.data[j] > key:
                self.data[j+1] = self.data[j]
                j -= 1
            self.data[j+1] = key
        return self.data

    def merge_sort(self):
        pass

    def quick_sort(self):
        pass


if __name__ == '__main__':
    # data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    data = [100, 60, 40, 70, 50, 20, 80, 90, 10]
    sr = Search(data)
    # print(sr.bubble_sort())
    # print(sr.binary_search(90))
    # print(sr.selection_sort())
    print(sr.insertion_sort())




