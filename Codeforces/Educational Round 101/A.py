
def is_rbs(s):
	arr = []
	if len(s)%2==1:
		return "NO"

	for i in s:
		if i=="(":
			arr.append(i)
		elif i==")":
			if len(arr)==0:
				return "NO"
			arr.pop()
		else:
			if len(arr)==0:
				arr.append("(")
			else:
				arr.pop()

	return "YES"

N = int(input())

for i in range(N):
	s = input()
	print(is_rbs(s))
