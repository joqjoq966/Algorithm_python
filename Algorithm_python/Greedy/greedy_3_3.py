s = input()

now = s[0]
n0 = 0; n1 = 0

for i in s:
	if i==now:
		pass
	else:
		if now =='0':
			n0+=1
		else:
			n1+=1
		now = i

if s[len(s)-1]=='0':
	n0+=1
else:
	n1+=1
print(min(n0,n1))
		 
