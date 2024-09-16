n = int(input())
array = list(map(int,input().split()))
answer = 0
while True:
    array.sort(reverse=True)
    if array[1] <= 0: break
    array[0] -= 1; array[1] -= 1
    answer += 1
print(answer)
