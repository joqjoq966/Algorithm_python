N,M = map(int, input().split())

answer = -1
for i in range(N):
	m = min(list(map(int, input().split())))
	if (answer<m):
		answer = m
print(answer)


# N,M = map(int, input().split())
# num = []
# for i in range(N):
# 	num.append(list(map(int, input().split())))

# answer = -1
# for i in range(N):
# 	_min = min(num[i])
# 	if answer<_min:
# 		answer = _min
# print(answer)