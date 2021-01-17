def solution(n,candy):
	w1=0; w2=0
	for i in candy:
		if i==1:
			w1+=1
		else:
			w2+=1
	if w1%2==1:
		return "NO"
	elif w1%2==0 and w2%2==0:
		return "YES"
	elif w1%2==0 and w2%2==1:
		if w1>=2:
			return "YES"
		return "NO"
	

t = int(input())
for i in range(t):
	n = int(input())
	candy = list(map(int,input().split()))

	print(solution(n,candy))
	
	