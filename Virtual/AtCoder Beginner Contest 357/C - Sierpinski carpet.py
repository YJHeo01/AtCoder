#재귀함수

import sys

sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    array = [['#']*(3**n) for _ in range(3**n)]
    solution(array,0,0,3**n,3**n)
    for i in range(3**n):
        for j in range(3**n):
            print(array[i][j],end="")
        print()

def solution(array,x1,y1,x2,y2):
    x_array = [x1,x1 + (x2-x1) // 3, x1 + (x2-x1) * 2 // 3, x2]
    y_array = [y1,y1 + (y2-y1) // 3, y1 + (y2-y1) * 2 // 3, y2]
    for i in range(x_array[1],x_array[2]):
        for j in range(y_array[1],y_array[2]):
            array[i][j] = '.'
    if x_array[2] - x_array[1] <=2:
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: continue
            solution(array,x_array[i],y_array[j],x_array[i+1],y_array[j+1])

if __name__ == "__main__":
    main()
