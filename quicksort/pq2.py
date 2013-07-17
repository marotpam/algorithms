def quick_sort(A):
    n = len(A)
    if n <= 1:
        return 0, A
    left = 0
    right = n
    comparisons += right -left
    p, A = partition(A,left, right)
    nL, L = quick_sort(A[left:p])
    nR, R = quick_sort(A[p:right])
    return n-1 + nL + nR, L+R 

def partition(A, l, r):
    p = A[l]
    i = l+1
    for j in range(i, r):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    return i, A

def main():
    global comparisons
    comparisons = 0
    n, A =  quick_sort([int(line) for line in open('pq2.in')])
    print comparisons

if __name__ == '__main__':
    main()
