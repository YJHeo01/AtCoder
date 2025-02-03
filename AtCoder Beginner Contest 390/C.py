from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [list(input().rstrip()) for _ in range(h)]
    
    global min_x, min_y, max_x, max_y
    min_x, min_y, max_x, max_y = h,w,-1,-1
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                min_x = min(min_x,i)
                min_y = min(min_y,j)
                max_x = max(max_x,i)
                max_y = max(max_y,j)
            if graph[i][j] == '?': cnt += 1

    if max_x == -1:
        if cnt == 0:print("No")
        else: print("Yes")
        return

    if graph[min_x][min_y] == '.':
        print("No")
        return
    
    visited = [[False]*w for _ in range(h)]
    answer = bfs(graph,visited,(min_x,min_y))
    if answer: print('Yes')
    else: print("No")
    
    

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < min_x or nx > max_x or ny < min_y or ny > max_y: continue
            if visited[nx][ny]: continue
            if graph[nx][ny] == '.': return False
            visited[nx][ny] = True
            queue.append((nx,ny))
    return True

if __name__ == "__main__":
    h,w = map(int,input().split())
    main()
