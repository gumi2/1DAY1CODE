'''
https://www.acmicpc.net/problem/13305
'''
# 기름값 : mon
# 거리 : dis
# 거리수 : N
# import sys
# N = int(input())
# dis = list(map(int,sys.stdin.readline().split()))
# mon = list(map(int,sys.stdin.readline().split()))
# cntlist = []
# now = mon[0]
# tdis = []
# cnt = 1
# for i in range(1,len(mon)):
#     if mon[0] == min(mon):
#         cnt = N-1
#         cntlist.append(cnt)
#         break
#     if i == len(mon)-1:
#         cnt += 1
#         cntlist.append(cnt)
#         break
#     if now <= mon[i]:
#         cnt +=1
#         continue
#     else:
#         now = mon[i]
#         cntlist.append(cnt)
#         cnt = 0
# print(cntlist)
# # for i in cntlist:
# #     result = 0
# #     for j in range(i):
# #         result += dis.pop(0)
# #         if j == i-1:
# #             tdis.append(result)
# # print(tdis)
# # -> 인덱스 에러 발생하는 이유가 pop쓸때 index가 커져서 그럼
# result = 0
# dis2 = dis
# realdis = []
# for i in cntlist:
#     for j in range(i):
#         result += dis2.pop(0)
#     realdis.append(result)
#     result = 0
# print(realdis)
# # result = 0
# # for i in range(len(cntlist)):
# #     result = result + mon[i]*tdis[i]
# # print(result)
# # for i in range(len(realdis)):
# #     if 처음은 :
# #         처음값 * 첫번째 realdis
# #     mon[cntlist]*
##############################
# 기름값 : mon
# 거리 : Dis
# 거리수 : N
import sys
N = int(input())
Dis = list(map(int,sys.stdin.readline().split()))
mon = list(map(int,sys.stdin.readline().split()))
m = mon[0]
result = 0
for i in range(N-1):
    if m > mon[i]:
        m = mon[i]
    result += m * Dis[i]
print(result)
# -> 어려운풀이로도 풀어보기
