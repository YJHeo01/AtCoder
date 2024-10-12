import sys, math

input = sys.stdin.readline

n = int(input())
array = [[0,0]]
for _ in range(n):
    array.append(list(map(int,input().split())))
array.append([0,0])
answer = 0
for i in range(1,n+2):
    a,b = array[i-1]
    c,d = array[i]
    answer += math.sqrt((a-c)**2+(b-d)**2)

print(answer)
