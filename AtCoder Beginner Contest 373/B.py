position = {}

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in s:
    position[i] = 0

tmp = list(input())

for i in range(26):
    position[tmp[i]] = i

answer = 0

for i in range(1,26):
    answer += abs(position[s[i]]-position[s[i-1]])

print(answer)
