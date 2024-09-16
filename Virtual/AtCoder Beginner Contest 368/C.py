n = int(input())

hp = list(map(int,input().split()))

t = 0

for i in range(n):
    while True:
        if hp[i] <= 0 or t % 3 == 0: break
        if t % 3 == 1: hp[i] -= 1
        else: hp[i] -= 3
        t += 1
    tmp = hp[i] // 5
    t += 3 * tmp
    hp[i] -= tmp * 5
    while True:
        if hp[i] <= 0: break
        if t % 3 == 2: hp[i] -= 3
        else: hp[i] -= 1
        t += 1

print(t)
