class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"  # New nodes are red by default
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = "BLACK"
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def __rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def __rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def __fix_insert(self, k):
        while k != self.root and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "RED":
                    # Case 1
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # Case 2
                        k = k.parent
                        self.__rotate_left(k)
                    # Case 3
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.__rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.__rotate_right(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.__rotate_left(k.parent.parent)
        self.root.color = "BLACK"

    def insert(self, key):
        node = Node(key)
        node.left = self.NULL
        node.right = self.NULL

        y = None
        x = self.root

        while x != self.NULL:
            y = x
            if node.data < x.data:
                x = x.left
            elif node.data > x.data:
                x = x.right
            else:
                print("Duplicate value not allowed.")
                return

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "BLACK"
            return

        self.__fix_insert(node)

    def __minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def __fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.__rotate_left(x.parent)
                    s = x.parent.right
                if s.left.color == "BLACK" and s.right.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.right.color == "BLACK":
                        s.left.color = "BLACK"
                        s.color = "RED"
                        self.__rotate_right(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.right.color = "BLACK"
                    self.__rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.__rotate_right(x.parent)
                    s = x.parent.left
                if s.right.color == "BLACK" and s.left.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.left.color == "BLACK":
                        s.right.color = "BLACK"
                        s.color = "RED"
                        self.__rotate_left(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.left.color = "BLACK"
                    self.__rotate_right(x.parent)
                    x = self.root
        x.color = "BLACK"

    def __delete_node_helper(self, node, key):
        z = self.NULL
        while node != self.NULL:
            if node.data == key:
                z = node
                break
            elif key < node.data:
                node = node.left
            else:
                node = node.right

        if z == self.NULL:
            print("Node not found")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.__minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "BLACK":
            self.__fix_delete(x)

    def __rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, key):
        self.__delete_node_helper(self.root, key)

    def search(self, key):
        def _search(node):
            if node == self.NULL or key == node.data:
                return node != self.NULL
            if key < node.data:
                return _search(node.left)
            return _search(node.right)
        return _search(self.root)

    def inorder(self, node):
        if node != self.NULL:
            self.inorder(node.left)
            print(f"{node.data}({node.color})", end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node != self.NULL:
            print(f"{node.data}({node.color})", end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node != self.NULL:
            self.postorder(node.left)
            self.postorder(node.right)
            print(f"{node.data}({node.color})", end=" ")

if __name__ == "__main__":
    rbt = RedBlackTree()

    while True:
        print("\n--- Red-Black Tree Menu ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Inorder Traversal")
        print("5. Preorder Traversal")
        print("6. Postorder Traversal")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            rbt.insert(val)
        elif choice == '2':
            val = int(input("Enter value to delete: "))
            rbt.delete(val)
        elif choice == '3':
            val = int(input("Enter value to search: "))
            found = rbt.search(val)
            print("Found" if found else "Not Found")
        elif choice == '4':
            print("Inorder traversal: ", end="")
            rbt.inorder(rbt.root)
            print()
        elif choice == '5':
            print("Preorder traversal: ", end="")
            rbt.preorder(rbt.root)
            print()
        elif choice == '6':
            print("Postorder traversal: ", end="")
            rbt.postorder(rbt.root)
            print()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
