import sys as s
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.head = self.tail = new_node  
        else:
            self.temp = self.head
            self.head = new_node
            self.head.next = self.temp

            # self.tail.next = new_node
            # self.tail = new_node


    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return None
        self.temp = None
        while self.temp == self.head
        # removed_data = self.head.data
        # self.head = self.head.next
        # if self.head is None:  
        #     self.tail = None
        # return removed_data

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
            q.enqueue()
        case 2:
             q.dequeue()
        case 3:
            q.display()
        case 4:
            q.exit_program()
        case _:
            print('Invalid choice')

while True:
    print('1:Enqueue 2.Dequeue 3.Display 4:Exit')
    choice = int(input('Your choice Plz: '))
    if choice == 1:
        e = int(input("Enter the element to Enqueue: "))
        q.enqueue(e)
    else:
        c = menu_choice(choice)
        