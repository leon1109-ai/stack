import time

def my_function(n):
    result = 0
    for i in range(100000000):
        result += i/n
    return result


start = time.time()
args = [1, 2, 3, 4, 5]
for x in args:
    result = map(my_function, args)
end = time.time()
#print(futures)
print(end - start)