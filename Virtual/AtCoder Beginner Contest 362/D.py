import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    weight = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,b = map(int,input().split())
        graph[u].append((v,b))
        graph[v].append((u,b))
    INF = int(1e9) * int(1e6)
    distance = [INF] * (n+1)
    dijkstra(graph,distance,weight)
    for i in range(2,n+1):
        print(distance[i],end=" ")

def dijkstra(graph,distance,weight):
    q = []
    distance[1] = weight[1]
    heapq.heappush(q,(weight[1],1))
    while q:
        vd, vx = heapq.heappop(q)
        if vd > distance[vx]: continue
        for nx, dd in graph[vx]:
            nd = vd + dd + weight[nx]
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

if __name__ == "__main__":
    main()
