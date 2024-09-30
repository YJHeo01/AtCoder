h,w = map(int,input().split())
x,y = map(int,input().split())

graph = [[]]

for _ in range(h):
    graph.append([0]+list(input()))

command = list(input())

for c in command:
    if c == 'L':
        if y != 1 and graph[x][y-1] == '.': y -= 1
    elif c == 'R':
        if y != w and graph[x][y+1] == '.': y += 1
    elif c == 'U':
        if x != 1 and graph[x-1][y] == '.': x -= 1
    else:
        if x != h and graph[x+1][y] == '.': x += 1
    
print(x,y)
