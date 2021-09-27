'''종이의 개수
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	18421	10876	8177	58.857%
문제
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다. 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.

만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
(1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

출력
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.

예제 입력 1
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
예제 출력 1
10
12
11
https://www.acmicpc.net/problem/1780
'''

# 1. 각각 부위별로 잘라서 확인-> 같으면 pop -> i.count(1) 사용해서 개수확인

import sys
N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def cutting(paper):
    l = len(paper)
    k = l//3
    result = []
    for x in range(0,l,3):
        for y in range(0,l,3):
            ret = []
            for a in range(x,x+3):
                for b in range(y,y+3):
                    ret.append(paper[a][b])
            if ret.count(0) == 9:
                result.append(0)
            elif ret.count(-1) == 9:
                result.append(-1)

            elif ret.count(1) == 9:
                result.append(1)
            else:
                result.extend(ret)
    return result
a = []
a = cutting(matrix)
print(a.count(-1))
print(a.count(0))
print(a.count(1))
