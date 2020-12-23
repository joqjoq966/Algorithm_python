N,M,K = map(int,input().split())
num = list(map(int,input().split()))

ans = 0; _K=K 
num.sort(reverse = True) #제일 큰 두가지 원소만 사용
while M>0:
	if _K==0:
		ans += num[1]
		_K=K
	else:
		ans += num[0]
		_K-=1
	M-=1	
print(ans)