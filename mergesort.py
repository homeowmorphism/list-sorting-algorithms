def mergesort(l):
    print("Sorting", l)
    n = len(l)
    if n  > 1:
        left = l[:n/2]
        right = l[n/2:]
        mergesort(left)
        mergesort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1
           
        while i < len(left):
           l[k] = left[i]
           i += 1
           k += 1
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1 
    print l 

print "---"
print l
