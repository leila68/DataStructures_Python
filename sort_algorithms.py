
class Sort:
    def __init__(self, data):
        self.data = data
        self.size = len(self.data)

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

    def quick_sort(self):
        # Time Complexity: O(n log n) on average, O(n²) in the worst case.
        self.data = self._quick_sort_recursive(self.data)

    def _quick_sort_recursive(self, arr):
        if len(arr) <= 1:
            print('arr:', arr)
            return arr

        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]

        print('com', self._quick_sort_recursive(left) + [pivot] + self._quick_sort_recursive(right))
        return self._quick_sort_recursive(left) + [pivot] + self._quick_sort_recursive(right)

    def merge_sort(self):
        # n log(n)
        self.data = self._merge_sort_recursive(self.data)

    def _merge_sort_recursive(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self._merge_sort_recursive(arr[:mid])
        right_half = self._merge_sort_recursive(arr[mid:])

        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged


if __name__ == '__main__':
    # data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    data = [100, 60, 40, 70, 50, 20]
    print(data)
    so = Sort(data)
    # print(so.bubble_sort())
    # print(so.selection_sort())
    # print(so.insertion_sort())

    # so.quick_sort()
    # print("quick sorted Data:", sr.data)

    # so.merge_sort()
    # print("merge sorted Data:", sr.data)




