def main():
    n,m = map(int,input().split())
    popcorns = []
    for _ in range(n):
        popcorns.append(list(input()))
    answer = n
    for bit in range(1,2**(n+1)):
        visited = [False] * m
        cnt = 0
        for i in range(n):
            if (bit >> i) & 1:
                cnt += 1
                for j in range(m):
                    if popcorns[i][j] == 'o': visited[j] = True
        complete = True
        for i in range(m):
            if visited[i] == False:
                complete = False
                break
        if complete == True:
            answer = min(answer,cnt)
    print(answer)

if __name__  == "__main__":
    main()
