class Node:
    """Node for the linked list used in each bucket of the hash table."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Hash table implementation with separate chaining using linked lists."""
    def __init__(self, table_size=10):
        self.table = [None] * table_size
        self.size = 0

    def _hash(self, key):
        """Generate a hash index for the given key."""
        return hash(key) % len(self.table)

    def insert(self, key, value):
        """Insert or update a key-value pair in the hash table."""
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)
            self.size += 1

    def get(self, key):
        """Retrieve a value by its key."""
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False

    def print_table(self):
        """Print the hash table contents."""
        for i, node in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            current = node
            if not current:
                print("Empty")
            else:
                while current:
                    print(f"({current.key}, {current.value})", end=" -> ")
                    current = current.next
                print("None")


# Example usage
if __name__ == "__main__":
    ht = HashTable(5)
    ht.insert(1, "A")
    ht.insert(6, "B")
    ht.insert(11, "C")
    ht.insert(3, "D")

    print("Initial Hash Table:")
    ht.print_table()

    print("\nRetrieve key 6:", ht.get(6))  # Output: B
    print("Retrieve key 10:", ht.get(10))  # Output: None

    # ht.delete(6)
    print("\nHash Table after deleting key 6:")
    ht.print_table()
