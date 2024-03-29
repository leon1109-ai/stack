import sys

class Stacks:

    stack = []
    globals = {}

    def push(self, a):
        if '.' in a:
            a = float(a)
        elif a.isdecimal():
            a = int(a)
        
        self.stack.append(a)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            print('stack is empty')
            sys.exit()

    def add(self):
        self.stack.append(self.pop() + self.pop())

    def sub(self):
        self.stack.append(round(self.pop() - self.pop(), 4))

    def mul(self):
        self.stack.append(self.pop() * self.pop())

    def div(self):
        a = self.pop()
        b = self.pop()

        if isinstance(a, int) and isinstance(b, int):
            self.stack.append(a // b)
        else:    
            self.stack.append(round(a / b, 4))

    def print(self):
        print(self.pop())

    def equal(self):
        a = self.pop()
        b = self.pop()
        if a == b:
            self.push('TRUE')
        else:
            self.push('FALSE')

        return a

    def setglobal(self, a):
        self.globals[a] = self.pop()
    
    def getglobal(self, a):
        self.stack.append(self.globals[a])

    def setList(self, a, m, dict=globals):
        l = [0] * m
        dict[a] = l

    def setElement(self, a, i, dict=globals):
        array = dict[a]
        if i >= len(array):
            print('array is out of bounds')
            sys.exit()
        else:
            array[i] = self.pop()
            #print(dict)

    def getElement(self, a, i, dict=globals):
        array = dict[a]
        if i >= len(array):
            print('array is out of bounds')
            sys.exit()
        else:
            self.stack.append(array[i])
            #print(dict)

    def setlocal(self, a, dict):
        dict[a] = self.pop()
    
    def getlocal(self, a, dict):
        self.stack.append(dict[a])

    def funcReturn(self, dict):
        dict = {}
    
    def increment(self, var, local):
        local[var] += 1

    def decrement(self, var, local):
        local[var] -= 1




