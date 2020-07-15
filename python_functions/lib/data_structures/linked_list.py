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
