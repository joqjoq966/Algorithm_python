N = list(map(int,input()))

ans = 0
for i in range(len(N)//2): #제일 앞에 것은 더하고 뒤에 것은 빼면서 총 합이 0이 확인
	ans += N[i]
	ans -= N[-1-i]

if ans==0:
	print("LUCKY")
else:
	print("READY")

#시간 복잡도 : O(N)