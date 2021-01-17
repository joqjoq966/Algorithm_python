import math

def solution(s,t):
	ls = len(s)
	lt = len(t)

	if t*ls!=s*lt:
		return -1
		
	g = math.gcd(ls,lt)
	lcm = g*(ls//g)*(lt//g)
	
	if ls<lt:
		return (lcm//ls)*s
	else:
		return (lcm//lt)*t
	
q = int(input())

for i in range(q):
	s=input()
	t=input()
	print(solution(s,t))
