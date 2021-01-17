# 첫번째 풀이
def balanced(s):
	if 2*s.count(')')==len(s):
		return True
	return False
	
def correct(s):
	stack = []
	for i in s:
		if i=='(':
			stack.append(i)
		else:
			if len(stack)==0:
				return False
			else:
				stack.pop()
	return True

def solution(p):
	u=""
	v=""
	if len(p)==0:
		return ""

	for i in range(1,len(p)+1):
		if balanced(p[:i]):
			u = p[:i]
			v = p[i:]
			break
	
	if correct(u):
		u += solution(v)
	else:
		temp ="("
		temp +=solution(v)
		temp +=")"
		for i in range(len(u)):
			if u[i]=="(":
				u = u[:i]+")"+u[i+1:]
			else:
				u = u[:i]+"("+u[i+1:]
		
		u = temp + u[1:-1]
	return u

#################################################
# 두번째 풀이	
def correct(s):
    stack = []
    for i in range(len(s)):
        if(s[i]=='('):
            stack.append(s[i])
        else:
            if(len(stack)==0):
                return 0
            else:
                stack.pop()
    return 1

def balanced(s):
    l = 0
    r = 0
    for i in range(len(s)):
        if(s[i]=='l'):
            l+=1
        else:
            r+=1
    if(l==r):
        return 1
    else:
        return 0

def solution(p):
    answer = ''
    u=''; v=''
    left = 0; right = 0
    temp =''
    for i in range(len(p)):
        if(p[i]==')'):
            left+=1
        else:
            right+=1
        if(left==right and left>=1):
            u = p[:i+1]
            break
    v = p[len(u):]

    if(correct(u) and u!=''):
        return (u + solution(v))
    elif(u==''):
        return '' 
    else:
        temp +='('
        temp += solution(v)
        temp +=')'
        for i in range(1,len(u)-1):
            if(u[i]=='('):
                temp += ')'
            else:
                temp += '('
        return temp

    return answer