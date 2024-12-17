from itertools import combinations

h,w,d = map(int,input().split())

s = [list(input()) for _ in range(h)]

floor = []

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            floor.append((i,j))

test_case_list = list(combinations(floor,2))

answer = 0
for test_case in test_case_list:
    visited = [[False]*w for _ in range(h)]
    for x,y in test_case:
        for i in range(d+1):
            for dx in range(i+1):
                dy = i - dx
                for ddx, ddy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                    nx,ny = x + dx * ddx, y + dy * ddy
                    if nx < 0 or ny < 0 or nx >= h or ny >= w:
                        continue
                    visited[nx][ny] = True
    tmp = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] and s[i][j] == '.': tmp += 1
    answer = max(answer,tmp)

print(answer)
