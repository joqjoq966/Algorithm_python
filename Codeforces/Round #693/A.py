def solution(w,h,n):
	cnt1 = 1
	cnt2 = 1
	while True:
		if w%2==0:
			w//=2
			cnt1*=2
		else:
			break
	while True:
		if h%2==0:
			h//=2
			cnt2*=2
		else:
			break
	# print(cnt1,cnt2)
	if cnt1*cnt2>=n:
		return "Yes"
	return "NO"
	

t = int(input())
for i in range(t):
	w,h,n = map(int,input().split())
	print(solution(w,h,n))
	
	