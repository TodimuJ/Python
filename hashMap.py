class HashMap:
    def __init__(self, size):
        self.size = 6
        self.map = [None] * self.size
    
    def getHash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self.getHash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else: 
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] == value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.getHash(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.getHash(key)

        if self.map[key_hash] == None:
            return False
        
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print('-----PHONEBOOK------')
        for i in self.map:
            if i is not None:
                print(str(i))



h = HashMap(6)
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '567-3457')
h.add('Ankit', '256-5893')
h.add('Aditya', '569-2048')
h.add('Alicia', '143-2239')
h.add('Mike', '233-0047')
h.add('Aditya', '234-7098')
h.print()
h.delete('Bob')
h.print()
print('Ming:' + h.get('Ming'))