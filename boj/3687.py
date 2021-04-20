import sys
input = sys.stdin.readline

def solve(x):
    
    min_ans, max_ans = 0, 0
    if x <= 14:
        min_ans = dp[x]
    elif x % 7 == 3 :
        if x == 17:
            min_ans = 200 
        else:
            min_ans = int('200' + '8'*((x//7)-2))
    else:
        min_ans = str(dp[x-((x//7)-1)*7]) + '8'*(x//7 -1)
    
    if x % 2 == 0:
        max_ans = '1'*(x//2)
    else:
        max_ans = '7' + '1'*((x-3)//2)

    return min_ans, int(max_ans)
    
t = int(input())
dp = [0,0,1,7,4,2,6,8,10,18,22,20,28,68,88]
for _ in range(t):
    n = int(input())
    a,b = solve(n)
    print(a, b)