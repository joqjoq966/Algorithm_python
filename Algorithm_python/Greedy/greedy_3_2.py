s = list(map(int,input()))

answer = s[0]

for i in range(1,len(s)):
	if s[i]==0 or s[i]==1 or answer==0 or answer==1:
		answer+=s[i]
	else:
		answer*=s[i]

print(answer)

# 답 구하는 식을 만들고 그것을 계산
# op = []
# for i in range(len(s)-1):
# 	if s[i]==0 or s[i]==1 or answer==0:
# 		op.append('+')
# 	else:
# 		op.append('*')

# eq = ''
# for i in range(len(s)-1):
# 	eq+=str(s[i])+op[i]

# eq+=str(s[len(s)-1])

# print(eval(eq))
	
