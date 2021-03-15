def order(c):
    return ord(c)-ord('A')

s = input()
exist_cnt = []
latest_idx = []
ans = 0
cnt = 0
for _ in range(26):
    exist_cnt.append(0)
    latest_idx.append(-1)

for i, val in enumerate(s):
    now = i - latest_idx[order(val)]
    cnt += now - exist_cnt[order(val)]
    exist_cnt[order(val)] = now
    latest_idx[order(val)] = i
    ans+=cnt

print(ans)