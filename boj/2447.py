N = int(input())

def star(pattern):
    stars = []
    l = len(pattern)
    for i in range(3*len(pattern)):
        if i//len(pattern) == 1:
            stars.append(pattern[i%l] + " "*l + pattern[i%l])
        else:
            stars.append(pattern[i%l] * 3)
    return stars

pattern = ["***", "* *", "***"]

exp = 0
while True:
    if 3**(exp+1) == N:
        break
    exp+=1

for _ in range(exp):
    s = star(pattern)
    pattern = s

for i in range(len(pattern)):
    print(pattern[i])