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

    def find(self, key):
        for node in self.buckets:
            if node.key == key:
                return node.value

    def __hash_function(self, key):
        hashsum = 0
        for i in key:
            hashsum += (i + len(key))**ord(i)
        hashsum = hashsum % self.max_capacity
        return hashsum
