def fair(n):
	m = n
	while(m):
		y = m%10
		if y!=0 and n%y!=0:
			return False
		m//=10
	return True

t = int(input())
for i in range(t):
	n = int(input())

	while fair(n)!=True:
		n+=1
	print(n)

	# if fair(int(n),digit):
	# 	print(int(n))
	# else:
	# 	for i in range(int(n),10**18):
	# 		if fair(i,reversed(list(map(int,str(i))))):
	# 			print(i)
	# 			break
