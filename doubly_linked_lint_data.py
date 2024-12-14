
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
        pass

    def delete(self, data):
        pass

    def is_empty(self):
        return self.head is None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('\n')


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    # dll.insert_at_beginning(11)
    dll.display()
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    dll.insert_at_end(50)
    dll.display()
    dll.insert_at_position(44, 4)
    dll.display()
    print(dll.size)




