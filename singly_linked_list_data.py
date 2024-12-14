class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            self.size += 1

    def pre_append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append_at_position(self, data, position):
        current = self.head
        new_node = Node(data)
        prev = current
        curr_pos = 0
        if position > self.size:
            # print(f"Attempted to insert at position {position}, but it's invalid.")
            raise IndexError("Invalid position")
        while current:
            if curr_pos == position:
                new_node.next = current
                prev.next = new_node
                self.size += 1
                return True
            prev = current
            current = current.next
            curr_pos += 1
        return False

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def delete(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        previous = current
        while current:
            if current.data == data:
                previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        return False

    def is_empty(self):
        return self.head is None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('\n')


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.display()
    # print(ll.search(20))
    # print(ll.delete(50))
    ll.append(60)
    ll.display()
    print(ll.size)
    ll.pre_append(100)
    ll.display()
    print(ll.size)
    ll.append_at_position(70,3)
    ll.display()
    ll.append_at_position(80, 12)
    ll.display()
    print(ll.size)


