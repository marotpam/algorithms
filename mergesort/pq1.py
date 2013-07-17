def merge_sort(arr):
    middle = int(len(arr) / 2)
    if middle == 0:
        return 0, arr
    kleft, left = merge_sort(arr[:middle])
    kright, right = merge_sort(arr[middle:])
    k , merged = merge(left, right)
    return kleft+kright+k, merged

def merge(a,b):
    c = []
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]: 
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
            k+=len(a)-i
    c += a[i:] + b[j:]
    return k, c

if __name__ == "__main__":
    n, merged =  merge_sort([int(line) for line in open('pq1.in')])
    print n
