tmp = list(map(int,input().split()))

cnt = [0] * 5
for i in tmp: cnt[i] += 1

answer = 0

for i in range(1,5):
    answer += cnt[i] // 2

print(answer)
