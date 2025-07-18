#Implement Queue using list, insert at rear delete from front the list
import sys as s

def enqueue(l, e):
    l.insert(0, e)
    return l
def dequeue(l):
    if len(l) > 0:
        del l[0]
        return l
    else:
        return "Underflow"
def invalid(l):
    print('Invalid input')
def exit_program(l):
    s.exit('End of program')

options = {
    1 : enqueue,
    2 : dequeue,
    3 : invalid,
    4 : exit_program,
}

l = [3, 5, 6, 2, 4]
print("Queue is ", l)
while True:
    print('1:Enqueue 2.Dequeue 3:Exit')
    choice = int(input('Your choice Plz: '))
    if choice == 1:
        e = int(input("Enter the element to Enqueue: "))
        c = options.get(choice, invalid) (l, e)
        print(c)
    else:
        c = options.get(choice, invalid) (l)
        print(c)