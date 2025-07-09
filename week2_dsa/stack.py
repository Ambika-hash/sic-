import sys as s
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def push(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.head = self.tail = new_node  
        else:
            self.temp = self.head
            self.head = new_node
            self.head.next = self.temp

            # self.tail.next = new_node
            # self.tail = new_node


    def pop(self):
        if self.head is None:
            print("Queue is empty")
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:  
            self.tail = None
        return removed_data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <- ")
            current = current.next
        print("None")
    def exit_program(self):
        s.exit("End of Program")


q = Queue() 
def menu_choice(choice):
    match(choice):
        case 1:
            q.push()
        case 2:
             q.pop()
        case 3:
            q.display()
        case 4:
            q.exit_program()
        case _:
            print('Invalid choice')

while True:
    print('1:Push 2.Pop 3.Display 4:Exit')
    choice = int(input('Your choice Plz: '))
    if choice == 1:
        e = int(input("Enter the element to Push: "))
        q.push(e)
    else:
        c = menu_choice(choice)
        