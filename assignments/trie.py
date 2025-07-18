class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end_of_word

    def startsWith(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True


n = int(input())
trie = Trie()

for _ in range(n):
    parts = input().split()
    op = parts[0]
    word = parts[1]

    if op == "insert":
        trie.insert(word)
    elif op == "search":
        print("true" if trie.search(word) else "false")
    elif op == "startsWith":
        print("true" if trie.startsWith(word) else "false")
