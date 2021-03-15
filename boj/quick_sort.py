arr = [3,9,2,7,10,6,5,8,1]

def partition(arr,left,right):
    pivot = arr[left]
    i, j = left,right

    while i<j:
        while pivot < arr[j]:
            j-=1
        
        while i<j and pivot >= arr[i]:
            i+=1
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[left] = arr[i]
    arr[i] = pivot 
    return i

def quick_sort(arr,left,right):
    if left >= right:
        return
    
    pivot = partition(arr,left,right)
    quick_sort(arr,left,pivot-1)
    quick_sort(arr,pivot+1,right)

quick_sort(arr,0,len(arr)-1)
print(arr)