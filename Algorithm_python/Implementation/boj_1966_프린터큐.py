from collections import deque
import math

t = int(input())
for i in range(t):
	N,M = map(int,input().split())
	# 문서 입력
	q = deque(map(int,input().split()))
	# 타겟 값을 체크하기 위해 임시로 0.1을 더함
	q[M]+=0.1
	# 몇 번째로 출력되는 지 알기 위해 카운팅
	cnt = 0
	while True:
		# 큐의 제일 왼쪽값을 pop
		value = q.popleft()
		# 값이 실수인 경우(타겟 값인 경우)
		if value!=math.floor(value):
			# 큐가 비었거나, 나머지 값들보다 큰 경우 break 정답 출력
			if len(q)==0 or value>=max(q) :
				cnt+=1
				break
			# 아니면 다시 append
			else:
				q.append(value)
		# 값이 정수인 경우(타겟 값이 아닌 경우)
		else:
			# 값이 나머지 값들보다 큰 경우, 만약 타겟값이 max일 때는 floor를 씌워야 함
			if value>=math.floor(max(q)):
				cnt+=1
			# 아니면 다시 append
			else:
				q.append(value)
	# 출력순서 print
	print(cnt)

# from collections import deque
# t = int(input())
# for i in range(t):
# 	N,M = map(int,input().split())
# 	text = deque(map(int,input().split()))
# 	result = deque([0 for _ in range(N)])
# 	result[M]='target'
# 	cnt = 0
# 	while True:
# 		if text[0]==max(text):
# 			cnt +=1

# 			if result[0]=='target':
# 				print(cnt)
# 				break
# 			else:
# 				text.popleft()
# 				result.popleft()
# 		else:
# 			text.append(text.popleft())
# 			result.append(result.popleft())	
	
