import sys
import stacks as stacks
import time
from collections import deque
import numpy as np

isd = {
    'PUSH': 0,
    'POP': 1,
    'ADD': 2,
    'SUB': 3,
    'MUL': 4,
    'DIV': 5,
    'PRINT': 6,
    'EQUAL':7,
    'JUMP': 8,
    'JUMP_IF': 9,
    'CALL': 10,
    'RETURN': 11,
    'SETGLOBAL': 12,
    'GETGLOBAL': 13,
    'SETLOCAL': 14,
    'GETLOCAL': 15,
    'SETLIST': 16,
    'SETELEMETNT': 17,
    'GETELEMETNT': 18,
    'SETLOCALLIST': 19,
    'SETLOCALELEMETNT': 20,
    'GETLOCALELEMETNT': 21
}


#start = time.time()
args = sys.argv

# 
def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


with open(args[1], 'r') as f:
    list = f.read().split('\n')


jump_dic = {}

#print(list)
#s = time.time()
i = 0
while i < len(list):
    func = list[i]
    if '    ' in func:
        l = func.split('    ')
        list.insert(i, l[-1])
        list.remove(func)
    func = list[i]
    if ' ' in func:
        l = func.split(' ')
        for j in range(len(l) - 1, -1, -1):
            print(l[j])
            list.insert(i, l[j])
        #list.insert(i, l[0])
        i += 1
        list.remove(func)

    if ':' in list[i]:
        jump_dic[list[i]] = i

    i += 1
#e = time.time()
#print('time1 ', e - s)
#print(list)
#print(len(list))
#print(jump_dic)

# Stack
stack = stacks.Stacks()
pc = 0
lp = 0 #callした時の深さ
local = [{}]
back = []
end = []
flag = False
#count = 0
#debug = 30
#s = time.time()
while pc < len(list):
    l = list[pc]

    if pc == jump_dic.get(l):
        if not flag:
            #print(end)
            pc = end.pop() + 1
            continue

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
            #print()
            #print('if')
            #print(local[lp])
            pc = jump_dic[f'{list[pc+1]}:']
    elif l == 'CALL':
        #print(lp)
        #print()
        #print('call')
        #if debug == count:
        #    break
        #count += 1
        #print('stack: ', stack.stack)
        #print(local[lp])
        #print('end: ', end)
        #print(jump_dic)
        flag = True
        local.append({})
        back.append(pc + 1)
        pc = jump_dic[f'{list[pc+1]}:']
        lp += 1
    elif l == 'RETURN':
        #print()
        #print('return')
        flag = False
        end.append(pc)
        #print('back: ', back)
        pc = back.pop()
        lp -= 1
        #stack.funcReturn(local)
    elif l == 'SETLOCAL':
        stack.setlocal(list[pc+1], local[lp])
        pc += 1
    elif l == 'GETLOCAL':
        stack.getlocal(list[pc+1], local[lp])
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
    elif l == 'SETLOCALLIST':
        stack.setList(list[pc+1], int(list[pc+2]), local[lp])
        pc += 2
    elif l == 'SETLOCALELEMETNT':
        stack.setElement(list[pc+1], int(list[pc+2]), local[lp])
        pc += 2
    elif l == 'GETLOCALELEMETNT':
        stack.getElement(list[pc+1], int(list[pc+2]), local[lp])
        pc += 2
        

    pc += 1
#e = time.time()
#print('time2 ', e - s)
#print('count: ', count)
#end = time.time()
#print(end - start)
