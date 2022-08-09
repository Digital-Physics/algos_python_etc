class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# insert() and contains():
# time: O(log(n)) on balanced tree, O(n) in a worst case scenario (like if you're tree was one sided; you inserted in order)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value, curr_node=None):
        print("input value (may be a recursive call starting at non-root node)", value)
        if curr_node is None:
            if self.root is None:
                self.root = Node(value)
                return
            else:
                self.insert(value, self.root)
                return

        if value <= curr_node.value:
            if curr_node.left:
                self.insert(value, curr_node.left)
            else:
                curr_node.left = Node(value)
        else:
            if curr_node.right:
                self.insert(value, curr_node.right)
            else:
                curr_node.right = Node(value)

    def print_inorder(self, curr_node=None):
        if curr_node is None:
            curr_node = self.root
            if curr_node is None:
                raise Exception("The BSTree is empty")

        if curr_node.left:
            self.print_inorder(curr_node.left)
        print(curr_node.value)
        if curr_node.right:
            self.print_inorder(curr_node.right)

    def contains(self, value, curr_node=None):
        if curr_node is None:
            curr_node = self.root
            if curr_node is None:
                return False

        if value < curr_node.value:
            if curr_node.left:
                return self.contains(value, curr_node.left)
            else:
                return False
        elif value > curr_node.value:
            if curr_node.right:
                return self.contains(value, curr_node.right)
            else:
                return False
        else:
            return True


array_for_tree = [1, 6, 7, 2, 3, 10, 4, 8, 9, 7, 9]

bst = BinarySearchTree()
for val in array_for_tree:
    bst.insert(val)

print("contains 7?", bst.contains(7))
bst.insert(99)
print("contains 99?", bst.contains(99))
print("contains 77?", bst.contains(77))
bst.print_inorder()

# we should look at AVL trees, Red/Black trees, rebalancing, etc.
# we could create a tree so that it doesn't become lopsided so it doesn't degenerate to unbalanced O(n) tree
