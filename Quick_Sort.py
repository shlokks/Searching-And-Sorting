def main():
    A = []
    print("Enter the size of the list :")
    n = int(input())
    print("Enter the elements of the list :")
    A = list(map(int,input().split()))
    l,r = 0,n-1 
    QuickSort(A,l,r)
    print('Sorted list is : ',end = '')
    for i in range(n):
        print ("%d" %A[i],end = ' ')


def QuickSort(A,l,r):
    if l<r:
        q = Partition(A,l,r)
        QuickSort(A,l,q-1)
        QuickSort(A,q+1,r)
        

def Partition(A,l,r):
    pivot = A[l]
    i = r - 1
    for j in range(l,r):
        if A[j] >= pivot:
            i = i - 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]

    return (i+1)


if __name__ == "__main__" : main()