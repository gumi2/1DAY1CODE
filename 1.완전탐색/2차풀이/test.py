# from itertools import combinations
# # import itertools
# n = [1,2,3]
# # t = list(itertools.combinations(n,3))
# # print(t)
# t = list(combinations(n,2))
# for i in t: # i자체가 튜플이 된다.
#     print(i)

for i in range(3):
    print(i)
    for j in range(3):
        print(j)
        if j == 1:
            break
    print('a')
break 하면 현재 반복문 종료하고 다음으로 넘어감
