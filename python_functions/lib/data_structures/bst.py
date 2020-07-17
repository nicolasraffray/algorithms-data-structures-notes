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

    def return_all_elements(self):
        all_values = []

        # Traverse Left Tree
        if self.left:
            all_values += self.left.return_all_elements()
        # elif self.left is None:

        all_values.append(self.value)

        if self.right:
            all_values += self.right.return_all_elements()

        return all_values
