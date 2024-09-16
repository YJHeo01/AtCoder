from collections import deque
import sys, heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b); graph[b].append(a)
    node_list = list(map(int,input().split()))
    depth = [-1] * (n+1)
    bfs(graph,depth,node_list[0])
    visited = [False] * (n+1)
    q = []
    for node in node_list:
        visited[node] = True
        heapq.heappush(q,(depth[node],node))
    while q:
        tmp, vx = heapq.heappop(q)
        dfs(graph,visited,depth,vx)
    answer = 0
    for i in range(n+1):
        if visited[i] == True: answer += 1
    print(answer)

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == -1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

def dfs(graph,visited,depth,vx):
    for nx in graph[vx]:
        if depth[nx] > depth[vx]: continue
        if visited[nx] == True: return
        visited[nx] = True
        return dfs(graph,visited,depth,nx)

if __name__ == "__main__":
    main()
