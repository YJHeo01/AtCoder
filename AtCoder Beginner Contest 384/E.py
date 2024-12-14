#https://atcoder.jp/contests/abc384/submissions/60744463

import sys, heapq

input = sys.stdin.readline

h,w,x = map(int,input().split())

p,q = map(int,input().split())

array = [list(map(int,input().split())) for _ in range(h)]

def solution(graph,visited,start):
    q = []
    vx,vy = start
    visited[vx][vy] =True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = graph[vx][vy]
    heapq.heappush(q,(0,vx,vy))
    while q:
        s, vx, vy = heapq.heappop(q)
        if s * x >= ret_value:
            break
        ret_value += s
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                heapq.heappush(q,(graph[nx][ny],nx,ny))
    return ret_value

p -= 1; q -= 1

answer = solution(array,[[False]*w for _ in range(h)],(p,q))

print(answer)
