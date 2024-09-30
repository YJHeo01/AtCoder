from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [list(map(int,input().split())) for _ in range(h)]
    answer = h * w
    visited = [[False]*w for _ in range(h)]
    start_list = get_start(graph)
    for i in range(1,y+1):
        answer -= bfs(graph,visited,start_list[i],i)
        print(answer)

def get_start(graph):
    start = [[] for _ in range(10**5+1)]
    for vx in range(h):
        for vy in range(w):
            idx = graph[vx][vy]
            start[idx].append((vx,vy))
    return start

def bfs(graph,visited,start,high):
    queue = deque([])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = 0
    while start:
        vx,vy = start.pop()
        if visited[vx][vy] == True: continue
        new_start = False
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or visited[nx][ny] == True:
                new_start = True
                break
        if new_start == True:
            visited[vx][vy] = True
            queue.append((vx,vy))
            ret_value += 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
            if graph[nx][ny] <= high and visited[nx][ny] == False:
                visited[nx][ny] = True
                ret_value += 1
                queue.append((nx,ny))
    return ret_value

if __name__ == "__main__":
    h,w,y = map(int,input().split())
    main()
