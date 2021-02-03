class Node:
    def __init__ (self, children, isWord):
        self.children = children
        self.isWord = isWord

class Solution:
    def __init__(self)):
        self.trie = None

    def build(self, words):
        self.trie = Node(False, {})
        for word in words:
            current = self.trie
            for char in word:
                if not char in current.children:
                     current.children[char] = Node(False, {})
                 
    
    def autocomplete(self, prefix):
        return []
    

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge', 'dentist', 'fume'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']

