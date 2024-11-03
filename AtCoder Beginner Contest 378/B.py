n = int(input())
trash = [[]]

for _ in range(n):
    trash.append(list(map(int,input().split())))

q = int(input())

for _ in range(q):
    t,d = map(int,input().split())
    answer = (d // trash[t][0]) * trash[t][0] + trash[t][1]
    if answer < d: answer += trash[t][0]
    print(answer)
