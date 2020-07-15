class HashNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Hash():
    def __init__(self):
        pass

    def __hash_function(self):
        ''' Key is a string of characters. Hash function must convert this
        to integers. Uniformity is required '''
        # hashsum += (character index + key length)^character code
        # 0 < hashsum < length(internal array)
        # hashsum = hassum % capacity
        pass
