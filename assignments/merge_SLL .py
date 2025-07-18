class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def find_intersection(head1, head2):
    len1 = get_length(head1)
    len2 = get_length(head2)

    diff = abs(len1 - len2)

    if len1 > len2:
        for _ in range(diff):
            head1 = head1.next
    else:
        for _ in range(diff):
            head2 = head2.next

    while head1 and head2:
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next
    return None

# Example usage
common = Node(30)
common.next = Node(40)

a1 = Node(10)
a2 = Node(20)
a1.next = a2
a2.next = common

b1 = Node(15)
b1.next = common

result = find_intersection(a1, b1)
if result:
    print("Lists intersect at node with data:", result)
else:
    print("Lists do not intersect.")
