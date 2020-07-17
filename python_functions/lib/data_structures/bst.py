class BinarySearchTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_node(self, value):
        if value == self.value:
            return value
        # left tree
        if value < self.value:
            if self.left:
                self.left.add_node(value)
            else:
                self.left = BinarySearchTreeNode(value)
        # right tree
        if value > self.value:
            if self.right:
                self.right.add_node(value)
            else:
                self.right = BinarySearchTreeNode(value)
