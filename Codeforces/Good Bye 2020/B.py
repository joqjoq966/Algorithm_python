t = int(input())

for i in range(t):
	n = int(input())
	songs = list(map(int,input().split()))
	# songs.append(0)
	i = 0
	while i <len(songs):
		target = songs[i]
		cnt = 0
		while i<len(songs) and target == songs[i]:
			i+=1
			cnt+=1
		if cnt>=2:
			i-=1
			songs[i]+=1

	print(len(set(songs)))
	# 반복되는 거 iterating 하는 문제 참고!!!!
	

