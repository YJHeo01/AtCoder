n = int(input())
array = [-1] + list(map(int,input().split()))
num_dict = dict([])
for i in range(1,n+1):
    num = array[i]
    if array[i] not in num_dict:
        print(-1,end=" ")
    else:
        print(num_dict[array[i]],end=" ")
    num_dict[array[i]] = i
