class Node():

    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def get_list(self):
        show = ""
        display = self.head

        while display != None:
            show += str(display.value) + " "
            display = display.next

        return show

    def insert_at_start(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def insert_at_end(self, value):
        node = self.head
        if node == None:
            self.head == Node(value)
        else:
            while node.next != None:
                node = node.next
            node.next = Node(value)

    def insert_between(self, value, value_before_insertion):
        node = self.head
        if node == None:
            self.head == Node(value)
        while node.value != value_before_insertion:
            node = node.next
        node_after_insertion = node.next
        node.next = Node(value)
        node.next.next = node_after_insertion

    def del_node(self, value):
        node = self.head

        if node is not None:
            if node.value == value:
                self.head = node.next
                HeadVal = None
                return

        while node.next.value != value:
            node = node.next

        if (self.head == None):
            return

        node.next = node.next.next
