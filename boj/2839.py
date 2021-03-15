n = int(input())
max_5 = n//5
ans = -1
for i in range(max_5,-1,-1):
    if (n-5*i)%3==0:
        min_3 = (n-5*i)//3
        ans = i
        break
if ans==-1:
    print(-1)
else:
    print(min_3 + ans)