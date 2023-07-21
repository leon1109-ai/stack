from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# 非同期に実行する関数
def my_function(n):
    result = 0
    for i in range(100000000):
        result += i/n
    return result

# スレッドプールの作成
s = time.time()
with ProcessPoolExecutor() as executor:
    start = time.time()
    args = [1, 2, 3, 4, 5]
    result = executor.map(my_function, args)
    end = time.time()
e = time.time()
for x in result:
    print(x)
print(end - start)
print(e - s)
