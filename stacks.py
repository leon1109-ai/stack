import sys

class Stacks:

    stack = []
    local = {}

    def push(self, a):
        if '.' in a:
            a = float(a)
        elif a.isdecimal():
            a = int(a)
        
        self.stack.append(a)

    def pop(self):
        try:
            return self.stack.pop(-1)
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
        if self.pop() == self.pop():
            self.push('TRUE')
        else:
            self.push('FALSE')

    def setlocal(self, a):
        self.local[a] = self.pop()
    
    def getlocal(self, a):
        self.stack.append(self.local[a])

    



