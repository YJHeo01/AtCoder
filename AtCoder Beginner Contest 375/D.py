def main():
    s = list(input())
    length = len(s)
    idx_list = [[]for _ in range(26)]
    for i in range(length):
        idx_list[ord(s[i])-ord('A')].append(i)
    answer = 0
    for i in range(length):
        for alpha in range(26):
            answer += get_left_cnt(idx_list[alpha],i) * get_right_cnt(idx_list[alpha],i)
    print(answer)

def get_left_cnt(array,value):
    length = len(array)
    ret_value = 0
    left, right = 0,length-1
    while left <= right:
        mid = (left+right) // 2
        if array[mid] < value:
            ret_value = mid + 1
            left = mid + 1
            
        else:
            right = mid - 1
    return ret_value

def get_right_cnt(array,value):
    length = len(array)
    ret_value = length
    left, right = 0,length-1
    while left <= right:
        mid = (left+right) // 2
        if array[mid] > value:
            ret_value = mid
            right = mid - 1
        else:
            left = mid + 1
    return length - ret_value

if __name__ == "__main__":
    main()
