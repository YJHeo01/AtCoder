n = int(input())

array = list(map(int,input().split()))

if n == 2:
    print("Yes")
    exit(0)

answer = 'Yes'

for i in range(1,n-1):
    if array[i] ** 2 != array[i-1] * array[i+1]:
        answer = 'No'

print(answer)
