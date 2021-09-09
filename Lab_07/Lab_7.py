n = int(input("Enter a vlue for n: "))
L = [4,5,9,7,7,1,9,7,2]

def compute_f(n):
    if n == 0:
        return 2
    else:
        return compute_f(n-1)+2

def count_instances(L, x):
    if L == []:
        return 0
    if L[0] == x:
        return 1 + count_instances(L[1:], x)
    else:
        return 0 + count_instances(L[1:], x)

print("compute:")
print(compute_f(n))
print("\ncount instances:")
print(count_instances(L, 4))
print(count_instances(L, 7))
print(count_instances(L, 3))
print(count_instances(L, 9))