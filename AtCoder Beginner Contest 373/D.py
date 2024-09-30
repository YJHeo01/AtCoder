def main():
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,-w))
    visited = [False] * (n+1)
    answer = [0] * (n+1)
    for i in range(1,n+1):
        if visited[i]: continue
        stack = [i]
        visited[i] = True
        while stack:
            cur_node = stack.pop()
            for next_node,w in graph[cur_node]:
                if visited[next_node]: continue
                visited[next_node] = True
                answer[next_node] = answer[cur_node] + w
                stack.append(next_node)
    for i in answer[1:]:
        print(i,end=" ")
    

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
