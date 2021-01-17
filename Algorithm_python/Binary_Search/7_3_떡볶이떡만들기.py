import sys
input = sys.stdin.readline

def find_sum(arr,target):
	result = 0
	for item in arr:
		result += max(0,item-target)
	return result

# def binary_search(arr,target,start,end):
# 	while start<=end:
# 		min = (start+end)//2

# 		if arr[mid]==target:
# 			return mid
# 		elif target<arr[mid]:
# 			end = mid-1
# 		else:
# 			start = mid+1
# 	return None

N,M = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
end = max(arr)
result = 0
while start<=end:
	total = 0
	mid = (start+end)//2

	if find_sum(arr,mid) == M:
		result = mid
		break
	# 만약 잘랐을 때, 필요한 양 보다 더 적으면 자르는 높이를 더 줄인다(잘리는 부분의 합을 늘린다)
	elif find_sum(arr,mid) < M:
		end = mid-1
	# 필요한 양 보다 많으면 결과를 저장하고 자르는 높이를 늘린다(잘리는 부분의 합을 줄인다)
	else:
		result = mid
		start = mid+1

print(result)
