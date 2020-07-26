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

    # Breadth first traversal
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

    def pre_order_traversal(self):
        all_values = []

        all_values.append(self.value)

        if self.left:
            all_values += self.left.pre_order_traversal()

        if self.right:
            all_values += self.right.pre_order_traversal()

        return all_values

    def post_order_traversal(self):
        all_values = []

        if self.left:
            all_values += self.left.post_order_traversal()
        if self.right:
            all_values += self.right.post_order_traversal()
        all_values.append(self.value)

        return all_values

    def search(self, value):
        if self.value == value:
            return value
        # search left
        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        # search right
        if value > self.value:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.value
        if self.left:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.value
        if self.right:
            return self.right.find_max()

    def calculate_tree_sum(self):
        total = 0
        if self.left:
            total += self.left.calculate_tree_sum()
        total += self.value
        if self.right:
            total += self.right.calculate_tree_sum()
        return total

    def delete(self, data):
        if data < self.value:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.value:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.value = min_val
            self.right = self.right.delete(min_val)

        return self

    # todo post_order_traverse and pre_order_traverse
