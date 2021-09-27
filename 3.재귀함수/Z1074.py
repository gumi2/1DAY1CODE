'''Z
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	512 MB	31198	10263	7638	36.679%
문제
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.



만약, N > 1이 라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.



N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.



입력
첫째 줄에 정수 N, r, c가 주어진다.

출력
r행 c열을 몇 번째로 방문했는지 출력한다.

제한
1 ≤ N ≤ 15
0 ≤ r, c < 2N
예제 입력 1
2 3 1
예제 출력 1
11
예제 입력 2
3 7 7
예제 출력 2
63
https://www.acmicpc.net/problem/1074
'''
# def divide(size, start_row, start_col):
#     global cnt
#     if size == 2:
#         if start_row == r and start_col == c:  # 왼쪽 위
#             print(cnt)
#             return
#         cnt += 1
#         if start_row == r and start_col + 1 == c:  # 오른쪽 위
#             print(cnt)
#             return
#         cnt += 1
#         if start_row + 1 == r and start_col + 1 == c:  # 왼쪽 아래
#             print(cnt)
#             return
#         cnt += 1
#         if start_row + 1 == r and start_col + 1 == c:  # 오른쪽 아래
#             print(cnt)
#             return
#         cnt += 1
#     else:
#         divide(size // 2, start_row, start_col)
#         divide(size // 2, start_row, start_col + size // 2)
#         divide(size // 2, start_row + size // 2, start_col)
#         divide(size // 2, start_row + size // 2, start_col + size // 2)
#
# N, r, c = map(int, input().split())
# cnt = 0
# divide(2 ** N, 0, 0)
import sys
N , r, c = map(int, sys.stdin.readline().split())
cnt = 0
def divide(size, col, row):
    global cnt
    if size == 2:
        if col == c and row == r:
            print(cnt)
            return
        cnt +=1
        if col+1 ==c and row ==r:
            print(cnt)
            return
        cnt +=1
        if col == c and  row+1 == r:
            print(cnt)
            return
        cnt +=1
        if col +1 ==c and row+1 == r:
            print(cnt)
            return
        cnt +=1
    else:
        divide(size//2, col, row)
        divide(size//2, col + size//2, row)
        divide(size//2, col, row + size//2)
        divide(size//2, col + size//2, row+ size//2)

divide(2**N,0,0)
