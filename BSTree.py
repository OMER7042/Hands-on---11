class BasicBinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BasicBinarySearchTree:
    def __init__(self):
        self.root = None

    def basic_insert(self, key):
        self.root = self._basic_insert(self.root, key)

    def _basic_insert(self, node, key):
        if node is None:
            return BasicBinaryTreeNode(key)
        if key < node.key:
            node.left = self._basic_insert(node.left, key)
        elif key > node.key:
            node.right = self._basic_insert(node.right, key)
        return node

    def basic_search(self, key):
        return self._basic_search(self.root, key)

    def _basic_search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._basic_search(node.left, key)
        return self._basic_search(node.right, key)
    
    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key, end=" ")
            self._inorder_traversal(node.right)
# Test
bbst = BasicBinarySearchTree()
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for key in keys:
    bbst.basic_insert(key)

# assert bbst.basic_search(6).key == 6
# assert bbst.basic_search(12) is None
bbst.inorder_traversal()

#OUTPUT
C:\Users\OMER\Desktop\DAA codes>C:/Python311/python.exe "c:/Users/OMER/Desktop/DAA codes/BSTree.py"
1 3 4 6 7 8 10 13 14
