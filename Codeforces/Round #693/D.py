
def solution(n,arr):
	alice=0; bob=0
	arr_len = len(arr)
	arr.sort(reverse=True)
	for i in range(len(arr)):
		if i%2==0 and arr[i]%2==0:
			alice+=arr[i]
		elif i%2==1 and arr[i]%2==1:
			bob+=arr[i]
		
	if alice>bob:
		return "Alice"
	elif alice<bob:
		return "Bob"
	else:
		return "Tie"				


t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int,input().split()))
	print(solution(n,arr))
	
	