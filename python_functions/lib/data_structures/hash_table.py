class HashNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Hash():
    def __init__(self):
        self.max_capacity = 100
        self.size = 0
        self.buckets = [None] * self.max_capacity

    def insert(self, key, value):
        self.size += 1
        index = self.__hash_function(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = HashNode(key, value)
            return

        while node is not None:
            prev_node = node
            node = node.next

        if node is None:
            prev_node.next = HashNode(key, value)

    def find(self, key):
        for node in self.buckets:
            if node.key == key:
                return node.value

    def __hash_function(self, key):
        hashsum = 0
        for index, character in enumerate(key):
            hashsum += (index + len(key))**ord(character)
        hashsum = hashsum % self.max_capacity
        return hashsum
