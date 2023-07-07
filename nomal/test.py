a = 111
array = [0] * 5
array[2] = 12
array[1] = 11
print(array[2])

def func():
    c = 1 + 2
    return a * c

print(func())
def func2(a, b):
    array = [0] * 5
    array[0] = 5
    array[1] = a * b
    return array[0] + array[1]

print(func2(22, 11))
print('OWARI')

