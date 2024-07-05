#https://atcoder.jp/contests/abc360/submissions/55052992
s = list(input())

answer = "No"
r,m,S = -1,-1,-1
for i in range(3):
    if s[i] == 'R': r = i
    elif s[i] == 'S': S = i
    else: m = i
    
if r < m: answer = "Yes"

print(answer)
