import sys
input = sys.stdin.readline

def solve(n,b):
    a = "1"
    for i in range(1,n):
        if b[i]=="1":
            if a[i-1]=="1" and b[i-1]=="1":
                a+="0"
            else:
                a+="1"
        else:
            if a[i-1]==b[i-1]:
                a+="1"
            else:
                a+="0"

    return a

t = int(input())

for _ in range(t):
    n = int(input())
    b = sys.stdin.readline().rstrip()
    print(solve(n,b))
