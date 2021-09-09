A = set(['dog','cat','fish','frog'])
B = set([1,2,3,4,5,6])
f = set([('dog',1),('cat',1),('frog',5),('fish',4)])
g = set([('cat',1),('dog',1),('fish',5),('frog',4)])

def is_injective(A,B,f):
    print("\nChecking injective....")
    print('Domain A')
    print(A)
    print('Codomain B')
    print(B)
    for element in f: 
        a = element[0] 
        b = element[1] 
        for other in f:
            if other != element: 
                bprime = other[1] 
                if b == bprime:
                    return False
    return True  

check1 = is_injective(A,B,f)
if check1 == True:
    print('Function f is injective \n')
else:
     print('Function f is not injective \n')

# ========================================================
# Number 1
def equal_functions(f,g):
    print("Checking equal....")
    print('Function f:')
    print(f)
    print('Function g:')
    print(g)

    if (f == g):
        return True
    else:
        return False

check2 = equal_functions(f, g)
if check2 == True:
    print("Functions f and g are equal \n")
else:
    print("Functions f and g are not equal \n")

# ========================================================
# Number 2
def is_partial_function(A, f):
    print("Checking partial....")
    c = 0
    b = len(A)

    print('Set A:')
    print(A)
    print('Function f:')
    print(f)

    for element in f:
        a = element[0]

    i = len(a)
    while c != i:
        c += 1
    
    if c < b:
        return True
    
check3 = is_partial_function(A, f)
if check3 == True:
    print("function f is a partial function of A \n")
else:
    print("function f is not a partial function of A  \n")

# ========================================================
# Number 3

def composite_function(f, g):
    print("Checking composite....")
    j = set({})
    for element in f:
        for item in g:
            if element[1] == item[0]:
                j.add((element[0], item[1]))

    print("Function f:")
    print(f)
    print("Function g:")
    print(g)
    print("Composite function of f and g:")
    return j

f = set([('b', 4), ('a', 3), ('d', 1), ('c', 5)])
g = set([(2,'bird'),(4,'cat'),(3,'dog'),(4,'fish')])
print(composite_function(f, g))
