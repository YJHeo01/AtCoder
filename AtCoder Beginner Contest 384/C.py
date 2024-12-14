#https://atcoder.jp/contests/abc384/submissions/60732738
from itertools import combinations

score_list = []

array = list(map(int,input().split()))

text = ['A','B','C','D','E']
for i in range(1,6):
    data = list(range(5))
    test_case_list = list(combinations(data,i))
    for test_case in test_case_list:
        tmp_score = 0
        tmp_text = ""
        for i in test_case:
            tmp_score += array[i]
            tmp_text += text[i]
        score_list.append((tmp_score,tmp_text))

score_list = sorted(score_list,key=lambda x:(-x[0],x[1]))

for score, s in score_list:
    print(s)
