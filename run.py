import sys
import stacks

args = sys.argv

with open(args[1], 'r') as f:
    list = f.read().split('\n')

i = 0
while i < len(list):
    func = list[i]
    if ' ' in func:
        l = func.split(' ')
        list.insert(i, l[1])
        list.insert(i, l[0])
        i += 1
        list.remove(func)

    i += 1

# print(list)

# Stack
stack = stacks.Stacks()
i = 0
while i < len(list):
    l = list[i]
    if l == 'PUSH':
        stack.push(list[i+1])
        i += 1
    elif l == 'ADD':
        stack.add()
    elif l == 'SUB':
        stack.sub()
    elif l == 'MUL':
        stack.mul()
    elif l == 'PRINT':
        stack.print()
    elif l == 'POP':
        stack.pop()
    elif l == 'DIV':
        stack.div()
    else:
        print('ERROR')


    i += 1