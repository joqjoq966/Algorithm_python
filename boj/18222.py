k = int(input())

def find(x):
    i = 0
    while True:
        if 2**i >= x:
            break
        i+=1
    return 2**(i-1)

cnt = 0
while k > 8:
    k -= find(k)
    cnt += 1

x = [0,1,1,0,1,0,0,1]

if cnt%2 == 1:
    if x[k-1]==0:
        print(1)
    else:
        print(0)
else:
    print(x[k-1])