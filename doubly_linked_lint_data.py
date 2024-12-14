
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return True
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return self.size
        current = self.head
        while current.next:
            current = current.next
        new_node.prev = current
        current.next = new_node
        self.size += 1

    def insert_at_position(self, data, position):
        if position > self.size:
            print(f"Attempted to insert at position {position}, but it's invalid.")
            raise IndexError("Invalid position")

        new_node = Node(data)
        current = self.head
        previous = current

        pos = 0
        while current:
            if pos == position:
                current.prev = new_node
                new_node.next = current
                previous.next = new_node
                new_node.prev = previous
                self.size += 1
                return True
            previous = current
            current = current.next
            pos += 1
        return False

    def search(self, data):
        if self.head is None:
            return
        current = self.head
        pos = 1
        while current:
            if current.data == data:
                return pos
            current = current.next
            pos += 1

    def delete(self, data):
        current = self.head
        # if the del node is head
        if current.data == data:
            if current.next:
                current.next.prev = None
            self.head = current.next
            self.size -= 1
            return True
        while current:
            if current.data == data:
                if current.next:
                    # The prev pointer of the next node
                    current.next.prev = current.prev
                if current.prev:
                    # The next pointer of previous point
                    current.prev.next = current.next
                self.size -= 1
                return True
            current = current.next

    def is_empty(self):
        return self.head is None

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('\n')

    def print_backward(self):
        pass


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(11)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    dll.insert_at_end(50)
    dll.insert_at_position(44, 4)
    dll.print_forward()
    print(dll.size)
    # print(dll.search(40))
    print("delete", dll.delete(50))
    dll.print_forward()
    print(dll.size)





