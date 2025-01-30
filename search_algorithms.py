class Search:
    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def binary_search_tree(self, val):
        # Time Complexity: O(log n)
        left, right = 0, self.size - 1
        data = sorted(self.data)

        while left <= right:
            mid = (left + right) // 2
            if val == data[mid]:
                return data[mid]
            if val < data[mid]:
                right = mid - 1
            if val > data[mid]:
                left = mid + 1
        return 0

    def linear_search(self):
        # Time Complexity: O(n)
        pass

    def depth_first_search(self):
        # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
        pass

    def breadth_first_search(self):
        # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
        pass


if __name__ == '__main__':
    sr = Search()
