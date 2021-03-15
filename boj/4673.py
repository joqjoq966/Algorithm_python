exist = []
for i in range(1,10000):
    temp = i
    while i>=1:
        temp+=i%10
        i//=10
    exist.append(temp)
exist = set(exist)
ans = set([i for i in range(1,10000)])
ans = list(ans-exist)
ans.sort()


for i in ans:
    print(i)