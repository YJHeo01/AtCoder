h,w,k = map(int,input().split())

def dfs(graph,visited,start):
    x,y = start
    if visited[x][y] == k: return 1
    ret_value = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
        if visited[nx][ny] == -1 and graph[nx][ny] == '.':
            visited[nx][ny] = visited[x][y] + 1
            ret_value += dfs(graph,visited,(nx,ny))
            visited[nx][ny] = -1
    return ret_value

array = [list(input()) for _ in range(h)]


visited = [[-1]*w for _ in range(h)]

answer = 0

for i in range(h):
    for j in range(w):
        if array[i][j] == '.':
            visited[i][j] = 0
            answer += dfs(array,visited,(i,j))
            visited[i][j] = -1

print(answer)
