import sys
input = sys.stdin.readline

n,s,d = map(int,input().split())
x=[]
y=[]
ans = "No"
for _ in range(n):
    xx,yy = map(int,input().split())
    x.append(xx)
    y.append(yy)

for i in range(n):
    if x[i]<s and y[i]>d:
        ans = "Yes"
        break
print(ans)