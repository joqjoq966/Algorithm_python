import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
# dp = [1]*n
dp_up = [1]*n
dp_down = [1]*n
ans = 0 
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp_up[i] <= dp_up[j]:
            dp_up[i] += 1

for i in range(n-1,-1,-1):    
    for j in range(n-1,i,-1):
        if arr[i] > arr[j] and dp_down[i] <= dp_down[j]:
            dp_down[i] += 1

# print(dp_up)
# print(dp_down)
dp = [x+y for x,y in zip(dp_up,dp_down)]
ans = max(dp)-1
print(ans)
# 10
# 1 5 2 1 4 3 4 5 2 1