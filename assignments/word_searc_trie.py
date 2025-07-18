class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store the word at the end node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = word  # Mark end of word


def find_words(board, words):
    # Step 1: Build Trie
    trie = Trie()
    for word in words:
        trie.insert(word)

    rows, cols = len(board), len(board[0])
    result = set()
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c, node):
        char = board[r][c]
        if char not in node.children:
            return

        visited[r][c] = True
        next_node = node.children[char]

        if next_node.word:
            result.add(next_node.word)

        # Explore neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                dfs(nr, nc, next_node)

        visited[r][c] = False  # Backtrack

    # Step 2: Start DFS from each cell
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, trie.root)

    return result


m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(input().split())

k = int(input())
words = [input().strip() for _ in range(k)]


found_words = find_words(board, words)
for word in found_words:
    print(word)
