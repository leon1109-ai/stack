import sys
import stacks as stacks
import time

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
            #print(l[j])
            list.insert(i, l[j])
        #list.insert(i, l[0])
        i += 1
        list.remove(func)

    #print(func)
    if ':' in list[i]:
        jump_dic[list[i]] = i
    elif 'JUMP' in func:
        jump_dic[list[i]] = i
        #print(list[i])
    elif ';' in list[i]:
        jump_dic[list[i]] = i
        

    i += 1
#e = time.time()
#print('time1 ', e - s)
print(list)
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
loopEnd = -1
#count = 0
#debug = 30
s = time.time()
while pc < len(list):
    l = list[pc]

    #ラベル部分を飛ぶ
    if pc == jump_dic.get(l):
        if not flag and my_index(end, pc):
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
        skip = stack.equal()
    elif l == 'SETGLOBAL':
        stack.setglobal(list[pc+1])
        pc += 1
    elif l == 'GETGLOBAL':
        stack.getglobal(list[pc+1])
        pc += 1
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
    elif l == 'JUMP':
        #print(local[lp][f'{list[pc - 1]}'])
        loopEnd = pc - 5
        pc = jump_dic[f'{list[pc+1]};']
        if not local[lp][f'{list[pc - 1]}'] == skip:
            pc = pc+7
    elif l == 'JUMP_IF':
        if stack.pop() == 'TRUE':
            #print()
            #print('if')
            #print(local[lp])
            pc = jump_dic[f'{list[pc+1]};']
    elif l == 'INCREMENT':
        stack.increment(list[pc+1], local[lp])
        pc += 1
    elif l == 'DECREMENT':
        stack.decrement(list[pc+1], local[lp])
        pc += 1

    pc += 1
e = time.time()
print('time2 ', e - s)
#print('count: ', count)
#end = time.time()
#print(end - start)
