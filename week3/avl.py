class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Helper functions
def get_height(node):
    return 0 if not node else node.height

def get_balance(node):
    return 0 if not node else get_height(node.left) - get_height(node.right)

# Rotations
def right_rotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

# Insert
def insert(root, key):
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Balancing cases
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Get min value node in a subtree
def get_min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Delete
def delete(root, key):
    if not root:
        return root
    elif key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node with one or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # Node with two children
        temp = get_min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    if not root:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Rebalancing
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Pre-order traversal
def preorder(node):
    if not node:
        return []
    return [node.key] + preorder(node.left) + preorder(node.right)

# Driver code
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    root = None
    for key in arr:
        root = insert(root, key)

    # Example deletion (uncomment below to test delete)
    # delete_values = list(map(int, input("Enter keys to delete: ").split()))
    # for val in delete_values:
    #     root = delete(root, val)

    print("Preorder after all insertions:")
    print(" ".join(map(str, preorder(root))))
