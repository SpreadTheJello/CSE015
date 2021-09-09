# Example sets (feel free to change to whatever to test)
A = set([1,2,3,4])
B = set(['D','B','C'])
f = set([(1,'D'),(2,'B'),(3,'C'),(4,'C')])

# checks to see if set is a graph
def is_a_graph(A,B,f):
    for element in f:
        b = element[0] 
        for other in f: 
            if other != element: 
                bprime = other[0]
                if b == bprime:
                    return False
    return True  

# checks to see if set is injective
def is_injective(A,B,f):
    for element in f: 
        a = element[0] 
        b = element[1] 
        for other in f:
            if other != element: 
                bprime = other[1]
                if b == bprime:
                    return False
    return True  

# checks to see if set is surjective
def is_surjective(A,B,f):
    for element in B:
        count = 0
        b = element
        for other in f:
            count += other.count(b)
        if count == 0:
            return False
    return True
    
# tells user if function is a graph
check1 = is_a_graph(A,B,f)
if check1 == True:
    print("Function f is a graph")
else:
    print("Function f is not a graph")

# tells user if function is bijective, injective, or surjective
check2 = is_injective(A,B,f)
check3 = is_surjective(A,B,f)
if check2 == check3:
    print('Function f is bijective (both injective and surjective')
else:
    if check2 == True:
        print('Function f is injective')
    else:
         print('Function f is not injective')

    if check3 == True:
        print("Function f is surjective")
    else:
        print("Function f is not surjective")
