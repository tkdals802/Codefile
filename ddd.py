import random

def make_heap(A,n):
    print(2)
    for i in range(n-1,-1,-1):
        heapify_down(A,i,n)

def heapify_down(A,k,n):
    print(3)
    while 2*k+1 < n:
        L,R=2*k+1, 2*k+2
        if L<n and A[k]<A[L]:
            m=L
        else:
            m=k
        if R<n and A[m]<A[R]:
            m=R
        if m!=k:
            A[k],A[m]=A[m],A[k]
            k=m
        else:
            break
        

def heap_sort(A):
    print(1)
    n=len(A)
    make_heap(A,n)
    for i in range(n):
        heapify_down(A,0,n-i)
        A[0],A[n-i-1]=A[n-i-1],A[0]
        




A=[]
for i in range(50):
    A.append(random.randint(1,100))
heap_sort(A)
print(A)











