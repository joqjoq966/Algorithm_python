def solution(n):
	s1 = "8901234567"
	if  n==1:
		return 9
	
	return "9"+((n-1)//10)*s1 + s1[:(n-1)%10]
	
t = int(input())
for i in range(t):
	n = int(input())
	print(solution(n))
	
	