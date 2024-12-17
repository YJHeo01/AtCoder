water = 0

n = int(input())

cur_time = 0

for _ in range(n):
    t,v = map(int,input().split())
    for _ in range(cur_time,t):
        if water != 0: water -= 1
    cur_time = t
    water += v

print(water)
