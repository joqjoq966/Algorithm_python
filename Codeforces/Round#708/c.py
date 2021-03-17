import sys 
input = sys.stdin.readline

def solve(n,k):
    temp = n
    a = 1
    if n%2==0:
        while temp > 2 and temp%2==0:
            a *= 2
            temp//=2
        return a, (n-a)//2, (n-a)//2 
    else:
        return 1, (n-1)//2, (n-1)//2

t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    print(*solve(n,k))
	
