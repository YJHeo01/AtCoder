array = list(map(int,input().split()))

cnt = 0

while True:
    finish = True
    for i in range(1,5):
        if array[i-1] > array[i]:
            cnt += 1
            finish = False
            array[i-1], array[i] = array[i], array[i-1]
    if finish: break

if cnt == 1:print("Yes")
else: print("No")
