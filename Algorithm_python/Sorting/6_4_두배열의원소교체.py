N,K = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse = True)

for i in range(K):
	if a[i]>=b[i]:
		break
	else:
		a[i],b[i]=b[i],a[i]

print(sum(a))