# 해결 못함

N = int(input())
arr = [0,1,1]
idx = 1
n = 1

while len(arr) < 10:
    idx += 1
    arr.insert(idx,n)
    arr_len = len(arr)-1
    check = False
    
    for i in range(1,arr_len-1):
        for j in range(i+1, arr_len):
            if arr[i] != arr[j] or arr[i+1] != arr[j+1]:
                check = True
                break
        if check:
            break
    if not check:
        n += 1
    else:
        n = 1
    
print(arr)

