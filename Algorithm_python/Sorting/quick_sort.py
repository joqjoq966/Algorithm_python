arr = [1,7,8,2,9,10,3,4,6,5]

# 일반적인 퀵소트
def quick_sort(arr,start,end):
	if start>=end:
		return
	
	pivot = start
	left = start+1
	right = end

	while left <= right:
		while left <= end and arr[left] <= arr[pivot]:
			left += 1
		while right > start and arr[right] >= arr[pivot]:
			right -= 1
		
		if left > right:
			arr[pivot],arr[right] = arr[right],arr[pivot]
		else:
			arr[left],arr[right] = arr[right],arr[left]
	
	quick_sort(arr,start,right-1)
	quick_sort(arr,right+1,end)
quick_sort(arr,0,len(arr)-1)

# 파이써닉한 퀵소트
def quick_sort(arr):
	if len(arr)<=1:
		return arr

	pivot = arr[0]
	tail  = arr[1:]

	left = [x for x in tail if x < pivot]
	right = [x for x in tail if x >= pivot]

	return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(arr))
print(arr)
