'''수리공 항승
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	9062	3568	3042	39.404%
문제
항승이는 품질이 심각하게 나쁜 수도 파이프 회사의 수리공이다. 항승이는 세준 지하철 공사에서 물이 샌다는 소식을 듣고 수리를 하러 갔다.

파이프에서 물이 새는 곳은 신기하게도 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.

항승이는 길이가 L인 테이프를 무한개 가지고 있다.

항승이는 테이프를 이용해서 물을 막으려고 한다. 항승이는 항상 물을 막을 때, 적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다고 생각한다.

물이 새는 곳의 위치와, 항승이가 가지고 있는 테이프의 길이 L이 주어졌을 때, 항승이가 필요한 테이프의 최소 개수를 구하는 프로그램을 작성하시오. 테이프를 자를 수 없고, 테이프를 겹쳐서 붙이는 것도 가능하다.

입력
첫째 줄에 물이 새는 곳의 개수 N과 테이프의 길이 L이 주어진다. 둘째 줄에는 물이 새는 곳의 위치가 주어진다. N과 L은 1,000보다 작거나 같은 자연수이고, 물이 새는 곳의 위치는 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 항승이가 필요한 테이프의 개수를 출력한다.

예제 입력 1
4 2
1 2 100 101
예제 출력 1
2
https://www.acmicpc.net/problem/1449
'''
# -> 처음에N개 에서 빼줌
# -> 이줄 for 로 i 랑 i+1 로 각각 시작함
# -> 덮은거 만큼 i 에서 + 해서 시작
# ->i가 마지막에 도달하면 break 해줌
# 테이프 L , 개수 N , 점 p
# import sys
# N , L = map(int , sys.stdin.readline().split())
# p = list(map(int, sys.stdin.readline().split()))
# p.sort()
# cnt = 0
# for i in range(N):
#     i += cnt
#     if i >= N-1:
#         break
#     if p[i]-0.5 + L >= p[i+1] +0.5:
#         cnt +=1
#         for j in range(i+1,N):
#             if j+1 > N-1:
#                 break
#             if p[i]-0.5+L > p[j+1]+0.5:
#                 cnt += 1
# print(N-cnt)
'''나중에 이유찾기'''
import sys
N , L = map(int , sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
p.sort()
tape =1
end = p[0]-0.5 +L
for i in p:
    if end > i:
        continue
    else:
        tape +=1
        end = i-0.5+L
print(tape)
