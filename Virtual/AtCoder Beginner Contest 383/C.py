from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [list(input().rstrip()) for _ in range(h)]
    start = []
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 'H':
                start.append((i,j))
    visited = [[-1]*w for _ in range(h)]
    bfs(graph,visited,start)
    answer = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] < 0: continue
            if visited[i][j] <= d:
                answer += 1
    print(answer)
    
def bfs(graph,visited,start):
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == '#':
                continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

if __name__ == "__main__":
    h,w,d = map(int,input().split())
    main()
