def is_palindrome(s):
	for i in range(len(s)):
		if s[i]!=s[-1-i]:
			return False
	return True

def max_alpha(s):
	s = set(list(s))
	all = [chr(ord('a')+i) for i in range(26)]
	for i in range(len(all)):
		if all[i] not in s:
			return all[i]

t = int(input())
for _ in range(t):
	s = input()
	alpha = set(list(s))
	cnt = 0
	
	if is_palindrome(s) and len(s)>1:
		if len(s)%2==0:
			print("1")
			continue
		elif len(s)%2==1 :
			a = len(alpha)
			print(len(s)//2+2-a)
			continue

	for i in range(len(s)):
		for j in range(i+2,len(s)+1):
			if is_palindrome(s[i:j]):
				s = s[:j-1] + max_alpha(s) + s[j:]
				# print(s)
				cnt +=1
	print(cnt)