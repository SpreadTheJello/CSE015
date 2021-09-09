import random
import time

def gen_random_list(n):
    assert(n>0)
    li = [random.randint(0,10*n) for i in range(n)]
    return li

if __name__ == '__main__':
    l = gen_random_list(10)
    l.sort()
    print(l)

def linear_search(s,k):
    i = 0
    n = len(s) - 1

    while(i <= n and k != s[i]):
        i += 1
    if(i <= n):
        return -1

def binary_search(s,k):
    i = 0
    j = len(s)

    while i < j:
        mid = (i+j)//2
        if k > s[mid]:
            i = mid + 1
        else:
            j = mid
    if k == s[i]:
        result = i
    else:
        result = -1
    return result

print("\n\n")
print("Linear Search Times")
for i in range(9):
    li = gen_random_list(10**i)

    startTime = time.perf_counter()
    linear_search(li, -1)
    spentTime = time.perf_counter() - startTime

    print("Length = 10^" + str(i + 1))
    print(spentTime)

print("\n\n")
print("Binary Search Times")
for i in range(9):
    li = gen_random_list(10**i)

    startTime = time.perf_counter()
    binary_search(li, -1)
    spentTime = time.perf_counter() - startTime

    print("Length = 10^" + str(i + 1))
    print(spentTime)