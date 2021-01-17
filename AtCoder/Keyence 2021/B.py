import sys
input = sys.stdin.readline


n,k = map(int,input().split())
a = list(map(int,input().split()))
count = [0]*n
cnt=0
ans=0
for i in range(n):
	count[a[i]]+=1

while cnt<k:
	cnt+=1
	for i in range(n):
		if count[i]<cnt:
			ans+=i
			break
	
print(ans)



