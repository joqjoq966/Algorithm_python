i = int(input())

# 00:00:00 ~ 00:59:59 중 3이 등장하는 시간은 총 1575번
# 03:00:00 ~ 03:59:59 와 같이 '시'에 3이 들어가면 3600번

if i<3: 
	print(1575*(i+1))
elif 3<=i<13:
	print(1575*i+3600)
elif 13<=i<23:
	print(1575*(i-1)+3600*2)
else:
	print(1575*(i-2)+3600*3)
# 시간 복잡도 O(1)

# answer=0
# for i in range(N+1):
# 	for j in range(60):
# 		for k in range(60):
# 			if '3' in str(i) or '3' in str(j) or '3' in str(k):
# 				answer +=1
# 	print(answer)