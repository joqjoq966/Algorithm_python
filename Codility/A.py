def solution(A):
	i = 0
	size_list = [[0]*2*len(A)]
	cnt= 1
	while i<len(A)-1:
		if i<len(A)-1 and A[i]<A[i+1]:
			i+=1
			cnt += 1
		else:
			size_list[i]=cnt
			i+=1
			cnt = 1
	return size_list

print(solution([2,2,2,2,1,2,-1,2,1,3]))		


		
	
