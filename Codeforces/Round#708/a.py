import sys 
input = sys.stdin.readline

def solve(n,arr):
    count = [0]*101
    ans = []
    arr.sort()
    for i in arr:
        count[i] += 1
    for i in range(101):
        if count[i] >= 1:
            ans.append(i)
            count[i] -= 1
    
    for i in range(101):
        if count[i] > 0:
            while count[i]:
                ans.append(i)
                count[i] -= 1

    return ans

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(*solve(n, arr))
	