def main():
    
    A = []
    
    print("Enter the size of the list :")
    
    n = int(input())
    
    print("Enter the elements of the list :")
    
    A = list(map(int,input().split()))
    
    low,high = 0,n-1 
    
    QuickSort(A,low,high)
    
    print('Sorted list is :')
    print(A)
    


def QuickSort(A,low,high):
    
    if low < high:
        
        q = Partition(A,low,high)
        QuickSort(A,low,q-1)
        QuickSort(A,q+1,high)
        

def Partition(A,low,high):
    
    pivot_index = get_pivot(A,low,high)
    pivot_value = A[pivot_index]
    border = 0
    
    for i in range(low,high+1):
        
        if A[i] < pivot_value:
            
            border += 1
            A[i],A[border] = A[border],A[i]
            
    A[low],A[border] = A[border],A[low]
    
    return border


def get_pivot(A,low,high):
    
    mid = (low + high)//2
    pivot = high
    
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            pivot = mid
            
    if A[low] < A[high]:
        pivot = low
        
    return pivot


if __name__ == "__main__" : main()