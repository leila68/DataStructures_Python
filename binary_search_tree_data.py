# BST (Binary Search Tree)
# Left Subtree: left less than parent
# Right Subtree: right greater than the parent

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while current:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right

    def search(self, data):
        if self.root is None:
            return None
        current = self.root
        while current:
            if data == current.data:
                return current.data
            elif data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
        return None

    def min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, data):
        current = self.root
        parent = None

        # find the node to delete and its parent
        while current and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        if current is None:
            return None

        # delete when the node has no child
        if current.right is None and current.left is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # delete when node has two child
        elif current.right and current.left:
            successor = self.min_node(current.right)
            val = successor.data
            self.delete( successor.data)
            current.data = val

        # delete when node hase one child
        else:
            if current.left is not None:
                child = current.left
            else:
                child = current.right
            if current != self.root:
                if current == parent.left:
                    parent.data = child
                else:
                    parent.right = child
            else:
                self.root = child

    def inorder(self):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.data)
                traverse(node.right)

        traverse(self.root)
        return result


if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(15)
    bt.insert(25)
    bt.insert(8)
    bt.insert(16)
    print(bt.inorder())
    print(bt.search(18))
    bt.delete(16)
    print(bt.inorder())
