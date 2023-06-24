import sys
import stacks
import time


#start = time.time()
args = sys.argv

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


with open(args[1], 'r') as f:
    list = f.read().split('\n')


jump_dic = {}

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
        for j in range(len(l) - 1, -1, -1):
            list.insert(i, l[j])
        #list.insert(i, l[0])
        i += 1
        list.remove(func)

    if ':' in list[i]:
        jump_dic[list[i]] = i

    i += 1

#print(list)
#print(jump_dic)

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
    elif l == 'SETGLOBAL':
        stack.setglobal(list[pc+1])
        pc += 1
    elif l == 'GETGLOBAL':
        stack.getglobal(list[pc+1])
        pc += 1
    elif l == 'JUMP':
        pc = jump_dic[f'{list[pc+1]}:']
    elif l == 'JUMP_IF':
        if stack.pop() == 'TRUE':
            pc = jump_dic[f'{list[pc+1]}:']
    elif l == 'CALL':
        back = pc
        pc = jump_dic[f'{list[pc+1]}:']
    elif l == 'RETURN':
        end = pc
        pc = back
        stack.funcReturn()
    elif l == 'SETLOCAL':
        stack.setlocal(list[pc+1])
        pc += 1
    elif l == 'GETLOCAL':
        stack.getlocal(list[pc+1])
        pc += 1
    elif l == 'SETLIST':
        stack.setList(list[pc+1], int(list[pc+2]))
        pc += 2
    elif l == 'SETELEMETNT':
        stack.setElement(list[pc+1], int(list[pc+2]))
        pc += 2
    elif l == 'GETELEMETNT':
        stack.getElement(list[pc+1], int(list[pc+2]))
        pc += 2
        

    pc += 1


#end = time.time()
#print(end - start)
