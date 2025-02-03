import sys

input = sys.stdin.readline

def main():
    
    graph = [list(input().rstrip()) for _ in range(h)]
    
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

    answer = "Yes"

    for i in range(min_x,max_x+1):
        for j in range(min_y,max_y+1):
            if graph[i][j] == '.':
                answer = 'No'
    
    print(answer)

if __name__ == "__main__":
    h,w = map(int,input().split())
    main()
