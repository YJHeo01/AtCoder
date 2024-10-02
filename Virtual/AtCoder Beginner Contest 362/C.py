import sys

input = sys.stdin.readline

def main():
    n = int(input())
    L,R = [],[]
    prefix_sum_L = [0] * (n+1)
    prefix_sum_R = [0] * (n+1)
    for i in range(n):
        l,r = map(int,input().split())
        L.append(l); R.append(r)
        prefix_sum_L[i+1] = prefix_sum_L[i] + l
        prefix_sum_R[i+1] = prefix_sum_R[i] + r
    if sum(L) > 0 or sum(R) < 0:
        print("No")
        return
    print("Yes")
    value = 0
    array = [0] * n
    for i in range(n):
        if prefix_sum_R[n] - prefix_sum_R[i+1] + value + L[i] >= 0:
            array[i] = L[i]
            value += L[i]
        else:
            if prefix_sum_R[n] - prefix_sum_R[i+1] + value + R[i] > 0:
                target = R[i]
                left, right = L[i], R[i]
                while left <= right:
                    mid = (left+right) // 2
                    if prefix_sum_R[n] - prefix_sum_R[i+1] + value + mid >= 0:
                        target = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                value += target
                array[i] = target
            else:
                array[i] = R[i]
                value += R[i]
    print(*array)

if __name__ == "__main__":
    main()
