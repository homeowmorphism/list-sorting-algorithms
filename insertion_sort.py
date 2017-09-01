def insertion_sort(l):
    n = len(l)
    if n > 1:
        i = 1 
        while i < n:
            print ("Inserting", l[i], "into", l)
            j = i
            while j > 0:
                if l[j] < l[j-1]:
                    smaller = l[j]
                    bigger = l[j-1]
                    l[j-1] = smaller
                    l[j] = bigger
                j -= 1
                print l
            i += 1
            print "---"
