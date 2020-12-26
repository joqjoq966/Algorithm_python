N = int(input())
coins = list(map(int,input().split()))

coins.sort()
target=1

for i in range(N):
	if target < coins[i]:
		break
	target += coins[i]

print(target)

# 결과적으로는 간단한 아이디어지만 개인적으로는 어려운 아이디어라고 생각