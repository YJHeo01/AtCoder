#https://atcoder.jp/contests/abc375/submissions/60824856
#플루이드 워셜

import sys

input = sys.stdin.readline

def main():
    n,m,q = map(int,input().split())
    road_block_time = [-1] * m
    road_block_cnt = 0
    road_list = []
    block_road_list = []
    for _ in range(m):
        road_list.append(list(map(int,input().split())))
    query_list = [list(map(int,input().split())) for _ in range(q)]
    for query in query_list:
        if query[0] == 1:
            road_block_cnt += 1
            road_block_time[query[1]-1] = road_block_cnt
            block_road_list.append(query[1]-1)
    dist = [[[INF]*(n+1) for _ in range(n+1)]for _ in range(road_block_cnt+1)]
    for i in range(m):
        if road_block_time[i] == -1:
            a,b,c = road_list[i]
            dist[road_block_cnt][a][b] = min(c,dist[road_block_cnt][a][b])
            dist[road_block_cnt][b][a] = min(c,dist[road_block_cnt][b][a])
    for k in range(1,n+1):
        for x in range(1,n+1):
            for y in range(1,n+1):
                dist[road_block_cnt][x][y] = min(dist[road_block_cnt][x][y],dist[road_block_cnt][x][k]+dist[road_block_cnt][k][y])
    for i in range(road_block_cnt-1,-1,-1):
        idx = block_road_list.pop()
        a,b,c = road_list[idx]
        for x in range(1,n+1):
            for y in range(1,n+1):
                dist[i][x][y] = dist[i+1][x][y]
        dist[i][a][b] = min(dist[i][a][b],c)
        dist[i][b][a] = min(dist[i][b][a],c)
        for k in [a,b]:
            for x in range(1,n+1):
                for y in range(1,n+1):
                    dist[i][x][y] = min(dist[i][x][y],dist[i][x][k]+dist[i][k][y])
    road_block_cnt = 0
    for query in query_list:
        if query[0] == 1:
            road_block_cnt += 1
        else:
            e,x,y = query
            if dist[road_block_cnt][x][y] == INF:
                print(-1)
            else:
                print(dist[road_block_cnt][x][y])
        
if __name__ == "__main__":
    INF = int(1e15)
    main()
