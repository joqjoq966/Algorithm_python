def solution(s):
	if len(s)%2==1:
		return "NO"
	if s[0]==')' or s[-1]=='(':
		return "NO"
	return "YES"

	
t = int(input())

for i in range(t):
	s = input()
	print(solution(s))
	
	