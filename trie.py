class Node:
    def __init__ (self, children, isWord):
        self.children = children
        self.isWord = isWord

class Solution:
    def __init__(self):
        self.trie = None

    def build(self, words):
        self.trie = Node({}, False)
        for word in words:
            current = self.trie
            for char in word:
                if not char in current.children:
                     current.children[char] = Node({}, False)
                current = current.children[char]
            current.isWord = True 
                 
    
    def autocomplete(self, prefix):
        current = self.trie
        for char in prefix:
            if not char in current.children:
                return []
            current = current.children[char]
        
        return self.findWordsFromNode(current, prefix)

    def findWordsFromNode(self, node, prefix):
        words = []
        if node.isWord:
            words += [prefix]
        
        for char in node.children:
            words += self.findWordsFromNode(node.children[char], prefix + char)

        return words

    

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge', 'dentist', 'fume', 'doodle'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']

