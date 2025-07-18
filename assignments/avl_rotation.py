class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    print("RR Rotation at node", z.key)
    return y

def right_rotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    print("LL Rotation at node", z.key)
    return y

def insert(root, key):
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    # LL
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # RR
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # LR
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        print("LR Rotation at node", root.key)
        return right_rotate(root)

    # RL
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        print("RL Rotation at node", root.key)
        return left_rotate(root)

    return root


n = int(input())
arr = list(map(int, input().split()))
root = None
for val in arr:
    root = insert(root, val)
