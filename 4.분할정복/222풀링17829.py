'''222-풀링 출처
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	741	506	388	72.795%
문제
조기 졸업을 꿈꾸는 종욱이는 요즘 핫한 딥러닝을 공부하던 중, 이미지 처리에 흔히 쓰이는 합성곱 신경망(Convolutional Neural Network, CNN)의 풀링 연산에 영감을 받아 자신만의 풀링을 만들고 이를 222-풀링이라 부르기로 했다.

다음은 8×8 행렬이 주어졌다고 가정했을 때 222-풀링을 1회 적용하는 과정을 설명한 것이다

행렬을 2×2 정사각형으로 나눈다.



각 정사각형에서 2번째로 큰 수만 남긴다. 여기서 2번째로 큰 수란, 정사각형의 네 원소를 크기순으로 a4 ≤ a3 ≤ a2 ≤ a1 라 했을 때, 원소 a2를 뜻한다.



2번 과정에 의해 행렬의 크기가 줄어들게 된다.

종욱이는 N×N 행렬에 222-풀링을 반복해서 적용하여 크기를 1×1로 만들었을 때 어떤 값이 남아있을지 궁금해한다.

랩실 활동에 치여 삶이 사라진 종욱이를 애도하며 종욱이의 궁금증을 대신 해결해주자.

입력
첫째 줄에 N(2 ≤ N ≤ 1024)이 주어진다. N은 항상 2의 거듭제곱 꼴이다. (N=2K, 1 ≤ K ≤ 10)

다음 N개의 줄마다 각 행의 원소 N개가 차례대로 주어진다. 행렬의 모든 성분은 -10,000 이상 10,000 이하의 정수이다.

출력
마지막에 남은 수를 출력한다.

예제 입력 1
4
-6 -8 7 -4
-5 -5 14 11
11 11 -1 -1
4 9 -2 -4
예제 출력 1
11
예제 입력 2
8
-1 2 14 7 4 -5 8 9
10 6 23 2 -1 -1 7 11
9 3 5 -2 4 4 6 6
7 15 0 8 21 20 6 6
19 8 12 -8 4 5 2 9
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
예제 출력 2
17
https://www.acmicpc.net/problem/17829 (힌트존재)
'''
# import sys
# import math
#
#
# N = int(input())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
#
# def pooling(matrix):
#     l = len(matrix)
#     k = l // 2
#     ret = [[0] * k for _ in range(k)]
#     nx = 0
#     for x in range(0, l, 2):
#         ny = 0
#         for y in range(0, l, 2):
#             window = [matrix[x][y], matrix[x + 1][y], matrix[x][y + 1], matrix[x + 1][y + 1]]
#             window.sort(reverse=True)
#             ret[nx][ny] = window[1]
#             ny += 1
#         nx += 1
#
#     return ret

#
# def solution():
#     answer = matrix
#
#     for _ in range(int(math.log2(N))):k
#         answer = pooling(answer)
#
#     return answer[0][0]
#
#
# print(solution())

import sys
import math
N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# def pooling(matrix):
#     l = len(matrix)
#     k = l // 2
#     ret = [[0] * k for _ in range(k)]
#     nx = 0
    # for x in range(0, l, 2):
#         ny = 0
#         for y in range(0, l, 2):
#             window = [matrix[x][y], matrix[x + 1][y], matrix[x][y + 1], matrix[x + 1][y + 1]]
#             window.sort(reverse=True)
#             ret[nx][ny] = window[1]
#             ny += 1
#         nx += 1
#
#     return ret
def pooling(matrix1):
    l = len(matrix1)
    k = l//2
    ret = [[0]*k for _ in range(k)]
    nx = 0
    for x in range(0,l,2):
        ny = 0
        for y in range(0,l,2):
            arr = [matrix1[x][y], matrix1[x+1][y], matrix1[x][y+1], matrix1[x+1][y+1]]
            arr.sort()
            ret[nx][ny] = arr[2]
            ny +=1
        nx +=1 # 이거때문에 2시간은찾음 

    return ret

for _ in range(int(math.log2(N))):
    matrix = pooling(matrix)
print(matrix[0][0])
