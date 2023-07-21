import time

s = time.time()
i = 0
n = 100000
while i < n:
    a = 5 * i
    i += 1
#print('OWARI')
e = time.time()
print('time2 ', e - s)