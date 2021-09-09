
set = [1, 2]

def all_subsets(set):
    subset = [set.length]
    helper(set, subset, 0)

def helper(set, subset, i):
    if i == set.length:
        print_set(subset)
    else:
        subset[i] = None
        helper(set, subset, i+1)
        subset[i] = set[i]
        helper(set, subset, i+1)

def print_set(subset):
    print(set)
