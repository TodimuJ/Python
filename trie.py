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
        if len(prefix) < 2:
            return "Please input at least three letters"

        else:
            current = self.trie
            for char in prefix:
                if not char in current.children:
                    return []
                current = current.children[char]

            three = sorted(self.findWordsFromNode(current, prefix))[:3]
            normal = self.findWordsFromNode(current, prefix)

            return three

    def findWordsFromNode(self, node, prefix):
        words = []
        if node.isWord:
            words += [prefix]
        
        for char in node.children:
            words += self.findWordsFromNode(node.children[char], prefix + char)

        return words

    

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge', 'dentist', 'fume', 'doodle', 'dash', 'deal', 'deaf', 'destiny', 'deloitte', 'dealer', 'dew'])
print(s.autocomplete('d'))
# ['dog', 'door', 'dodge', 'doodle']

