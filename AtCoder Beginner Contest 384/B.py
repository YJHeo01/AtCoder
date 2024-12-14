#https://atcoder.jp/contests/abc384/submissions/60725794

n,r = map(int,input().split())

for _ in range(n):
    d,a = map(int,input().split())
    if d == 1:
        if r < 1600 or r >= 2800:continue
        r += a
    else:
        if r < 1200 or r >= 2400: continue
        r += a

print(r)
