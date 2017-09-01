import random

def quicksort(l):
    n = len(l)
    if n > 1:
        pivot_index = random.randint(0,n-1)
        pivot = l[pivot_index]
        left = []
        right = []
        pivot_clones = [pivot]
        for i in range(n):
            if i == pivot_index:
                pass
            elif l[i] < pivot:
               left.append(l[i])
            elif l[i] > pivot:
                right.append(l[i])
            else: 
                pivot_clones.append(l[i])
        return quicksort(left) + pivot_clones + quicksort(right)
    return l

x = [2,3,1]
print quicksort(x)
x = [3,2,1]
print quicksort(x)
x = [1,2,3]
print quicksort(x)
x = [0, -1]
print quicksort(x)
x = [0,0]
print quicksort(x)
