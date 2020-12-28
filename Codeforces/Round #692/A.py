def bad(s):
	r = 0
	for i in reversed(range(len(s))):
		if s[i]==')':
			r +=1
		else:
			return r
	return r

t = int(input())

for i in range(t):
	N = int(input())
	chat = input()
	b = bad(chat)
	if b > len(chat)-b:
		print("YES")
	else:
		print("NO")

