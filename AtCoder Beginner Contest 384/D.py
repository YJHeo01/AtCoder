#https://atcoder.jp/contests/abc384/submissions/60738839
n,s = map(int,input().split())

array = list(map(int,input().split()))

sum_array = sum(array)

s %= sum_array

left, right = 0,0

answer = 'No'

tmp = 0

while True:
    if right == n or left == n:
        break
    if tmp < s:
        tmp += array[right]
        right += 1
    elif tmp > s:
        tmp -= array[left]
        left += 1
    else:
        answer = 'Yes'
        break

s = sum_array - s

left, right = 0,0

tmp = 0

while True:
    if right == n or left == n:
        break
    if tmp < s:
        tmp += array[right]
        right += 1
    elif tmp > s:
        tmp -= array[left]
        left += 1
    else:
        answer = 'Yes'
        break

print(answer)
