arr = [3,9,2,7,10,6,5,8,1]

for i in range(1,len(arr)):
    temp = arr[i]
    prev = i-1
    while prev >= 0 and (arr[prev] > temp):
        arr[prev+1] = arr[prev]
        prev-=1
    arr[prev+1] = temp

print(arr)