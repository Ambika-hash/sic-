import sys as s

def push(l, e):
    l.insert(0, e)
    return l
def pop(l):
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
    1 : push,
    2 : pop,
    3 : invalid,
    4 : exit_program,
}

l = [3, 5, 6, 2, 4]
print("Stack is ", l)
while True:
    print('1:Push 2.Pop 3:Exit')
    choice = int(input('Your choice Plz: '))
    if choice == 1:
        e = int(input("Enter the element to push: "))
        c = options.get(choice, invalid) (l, e)
        print(c)
    else:
        c = options.get(choice, invalid) (l)
        print(c)