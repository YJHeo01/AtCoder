import sys

input = sys.stdin.readline

def main():
    array = [[]]
    for _ in range(n):
        array.append(['.']+list(input().rstrip()))
    for i in range(1,n//2+1):
        new_array = [['.']*(n+1) for _ in range(n+1)]
        for x in range(1,n+1):
            for y in range(1,n+1):
                turn_cnt = min(x,y,n-x+1,n-y+1)
                turn_cnt %= 4
                new_x, new_y = x,y
                for _ in range(turn_cnt):
                    new_x,new_y = turn(new_x,new_y)
                new_array[new_x][new_y] = array[x][y]
        array = new_array
        break
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(array[i][j],end="")
        print()

def turn(x,y):
    return y,n+1-x

if __name__ == "__main__":
    n = int(input())
    main()
