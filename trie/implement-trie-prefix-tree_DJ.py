class TrieNode:
    def __init__(self):
        self.isWord = False
        self.subnode = dict()

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if not char in node.subnode:
                node.subnode[char] = TrieNode()
            node = node.subnode[char]

        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if not char in node.subnode:
                return False
            node = node.subnode[char]

        return node.isWord == True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if not char in node.subnode:
                return False
            node = node.subnode[char]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)