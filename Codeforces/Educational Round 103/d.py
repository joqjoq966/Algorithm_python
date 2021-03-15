import sys
input = sys.stdin.readline

def solve(n,s):
    ans = [1]*(n+1)
    for i in range(n+1):
        l, r = i-1, i
        move = 0
        while l>=0:
            if move%2==0 and s[l]=="L":
                move += 1
                l-=1
            elif move%2==1 and s[l]=="R":
                move +=1
                l-=1
            else:
                break
        ans[i] += move
        move = 0
        while r<=n:
            if move%2==0 and s[r]=="R":
                move += 1
                r+=1
            elif move%2==1 and s[r]=="L":
                move +=1
                r+=1
            else:
                break
        ans[i] += move
    
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(*solve(n,s))
