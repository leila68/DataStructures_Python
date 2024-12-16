class ListData:
    def __init__(self):
        self.data = []

    def add_items(self, item):
        self.data.append(item)

    def reverse(self):
        start, end = 0, len(self.data) - 1
        while start < end:
            self.data[start], self.data[end] = self.data[end], self.data[start]
            start += 1
            end -= 1

    def rotate(self, k):
        k = k % len(self.data)

        def reverse(start, end):
            while start < end:
                self.data[start], self.data[end] = self.data[end], self.data[start]
                start += 1
                end -= 1
        reverse(0, len(self.data)-1)
        reverse(0, k-1)
        reverse(k, len(self.data)-1)

    def find_first_min_max(self):
        min_val = float('inf')
        max_val = float('-inf')
        for i in range(len(self.data)):
            if self.data[i] < min_val:
                min_val = self.data[i]
            if self.data[i] > max_val:
                max_val = self.data[i]
        return min_val, max_val

    def find_second_min_max(self):
        min_val, max_val = self.find_first_min_max()
        sec_min_val = float('inf')
        sec_max_val = float('-inf')

        for i in range(len(self.data)):
            if min_val < self.data[i] < sec_min_val:
                sec_min_val = self.data[i]
            if sec_max_val < self.data[i] < max_val:
                sec_max_val = self.data[i]

        return sec_min_val, sec_max_val

    # function to find second, third,... min and max
    def find_min_max(self, min_val, max_val):
        order_min_val = float('inf')
        order_max_val = float('-inf')

        for i in range(len(self.data)):
            if min_val < self.data[i] < order_min_val:
                order_min_val = self.data[i]
            if order_max_val < self.data[i] < max_val:
                order_max_val = self.data[i]

        return order_min_val, order_max_val

    def find_duplicates(self):
        duplicates = []
        for i in self.data:
            for j in self.data:
                if self.data[i] == self.data[j]:
                    duplicates.append(self.data[i])


if __name__ == '__main__':

    obj = ListData()
    obj.add_items(10)
    obj.add_items(35)
    obj.add_items(25)
    obj.add_items(65)
    obj.add_items(5)

    min, max = obj.find_first_min_max()
    print(min, max)

    # min, max = obj.find_second_min_max()
    # print(min, max)

    min2, max2 = obj.find_min_max(min, max)
    print(min2, max2)

    min3, max3 = obj.find_min_max(min2, max2)
    print(min3, max3)