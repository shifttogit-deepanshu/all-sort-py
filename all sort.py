A = [11,101,34,15,45,6,23,7,9,12,76] 

n = len(A)

#Selection Sort


def Selection_sort():
    for i in range(n):
        point = i
        for j in range(i+1,n):
            if A[j]<A[point]:
                point = j
    
        A[i],A[point] = A[point],A[i]
        
    print(A)

# Bubble Sort

def bubble_sort():
    n = len(A)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
        print(A)
                
    print(A)


def insertion_sort():
    for i in range(1,n):
        j = i-1
        key = A[i]
        while A[j]>key and j>=0:
            A[j+1]=A[j]
            A[j] = key           
            j=j-1
        key = A[j+1]
            
        
    print(A)
                

# Merge Sort        


def merge_sort(arr):   
    if len(arr) > 1:
        mid = len(arr)//2  
        
        L = arr[:mid]
        
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i=j=k=0
        while i< len(L) and j< len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i=i+1

            else:
                arr[k]=R[j]
                j+=1
            k+=1
            
        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1
            
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        
    print(arr)
        
# Quick Sort

def partition(arr,low,high):
    pivot = arr[high]
    
    i = low-1
    for j in range(low, high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
            
    arr[i+1],arr[high]=arr[high],arr[i+1]
    
    return i+1


def quick_sort(arr,low,high):
    if low<high: 
        pi = partition(arr,low,high)     
    
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
    
    print(arr)

 
quick_sort(A,0,len(A)-1)
        

    





















































