import sys
import stacks
import time


start = time.time()
args = sys.argv

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


with open(args[1], 'r') as f:
    list = f.read().split('\n')

#print(list)
i = 0
while i < len(list):
    func = list[i]
    if '    ' in func:
        l = func.split('    ')
        list.insert(i, l[len(l) - 1])
        list.remove(func)
    func = list[i]
    if ' ' in func:
        l = func.split(' ')
        list.insert(i, l[1])
        list.insert(i, l[0])
        i += 1
        list.remove(func)

    i += 1

#print(list)

# Stack
stack = stacks.Stacks()
pc = 0
back = 0
end = 0
while pc < len(list):
    l = list[pc]

    if pc == my_index(list, f'{list[back+1]}:'):
        pc = end

    if l == 'PUSH':
        stack.push(list[pc+1])
        pc += 1
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
    elif l == 'EQUAL':
        stack.equal()
    elif l == 'SETLOCAL':
        stack.setlocal(list[pc+1])
        pc += 1
    elif l == 'GETLOCAL':
        stack.getlocal(list[pc+1])
        pc += 1
    elif l == 'JUMP':
        pc = list.index(f'{list[pc+1]}:')
    elif l == 'JUMP_IF':
        if stack.pop() == 'TRUE':
            pc = list.index(f'{list[pc+1]}:')
    elif l == 'CALL':
        back = pc
        pc = list.index(f'{list[pc+1]}:')
    elif l == 'RETURN':
        end = pc
        pc = back

    pc += 1

end = time.time()
print(end - start)