n = int(input())
array = list(map(int,input().split()))
answer = n
left = 0
for right in range(1,n-1):
    if array[right] - array[right-1] != array[right+1] - array[right]:
        tmp = right - left
        answer += tmp * (tmp+1) // 2
        left = right

tmp = n - 1 - left
answer += tmp * (tmp+1) //2

print(answer)
