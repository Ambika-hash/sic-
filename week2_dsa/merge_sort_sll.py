class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other_list.head
def menu():
    list1 = LinkedList()
    list2 = LinkedList()
    list3 = LinkedList.merge()

    while True:
        print("\n--- MENU ---")
        print("1. Insert in List 1")
        print("2. Insert in List 2")
        print("3. Display List 1")
        print("4. Display List 2")
        print("5. Merge List 2 into List 1")
        print("6. Display Merged List")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter data to insert into List 1: "))
            list1.insert_end(data)

        elif choice == '2':
            data = int(input("Enter data to insert into List 2: "))
            list2.insert_end(data)

        elif choice == '3':
            print("List 1:", list1.display())

        elif choice == '4':
            print("List 2:", list2.display())

        elif choice == '5':
            list1.merge(list2)
            print("Merged List 2 into List 1.")

        elif choice == '6':
            print("Merged List:", list1.display())

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

menu()
