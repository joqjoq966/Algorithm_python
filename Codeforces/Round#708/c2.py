import sys 
input = sys.stdin.readline

def solve(n,k):
    ans =[]
    for _ in range(k-3):
        ans.append(1)
    n = n-(k-3)
    temp = n
    a = 1
    if n%2==0:
        while temp > 2 and temp%2==0:
            a *= 2
            temp//=2
        ans.append(a)
        ans.append((n-a)//2)
        ans.append((n-a)//2)
    else:
        ans.append(1)
        ans.append((n-1)//2)
        ans.append((n-1)//2)

    return ans
    

t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    print(*solve(n,k))
	
