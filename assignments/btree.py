class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.leaf = leaf
        self.keys = []  # List of keys
        self.children = []  # List of child pointers

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[-1].traverse()

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == k:
            return self
        if self.leaf:
            return None
        return self.children[i].search(k)

    def insert_non_full(self, k):
        i = len(self.keys) - 1

        if self.leaf:
            # Insert the key in sorted order
            self.keys.append(0)
            while i >= 0 and self.keys[i] > k:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = k
        else:
            # Find child to insert the key
            while i >= 0 and self.keys[i] > k:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if k > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(k)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        z.keys = y.keys[t:]  # Right half
        y.keys = y.keys[:t - 1]  # Left half

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t

    def traverse(self):
        if self.root:
            self.root.traverse()
        else:
            print("Tree is empty.")

    def search(self, k):
        return self.root.search(k) if self.root else None

    def insert(self, k):
        if not self.root:
            self.root = BTreeNode(self.t, True)
            self.root.keys = [k]
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                s = BTreeNode(self.t, False)
                s.children.append(self.root)
                s.split_child(0)
                i = 0
                if s.keys[0] < k:
                    i += 1
                s.children[i].insert_non_full(k)
                self.root = s
            else:
                self.root.insert_non_full(k)
if __name__ == "__main__":
    print("Creating a B-Tree of minimum degree 2 (t=2)...")
    btree = BTree(2)

    for val in [10, 20, 5, 6, 12, 30, 7, 17]:
        btree.insert(val)

    print("Traversal of B-Tree:")
    btree.traverse()
    print()

    key = 12
    print(f"Searching for key {key}:")
    result = btree.search(key)
    print("Found!" if result else "Not Found.")
