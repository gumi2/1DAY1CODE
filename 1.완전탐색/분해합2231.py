'''분해합
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	192 MB	51547	24633	19574	47.399%
문제
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

예제 입력 1
216
예제 출력 1
198
https://www.acmicpc.net/problem/2231
'''
# N = int(input())
# i = 0
# t = N
# while True:
#     if (t <10):
#         i += 1
#         break
#     t = t/10
#     i +=1
# if(N<9):
#     print(0)
#     exit()
# for j in range(N-9*i,N):
#     result = 0
#     result = j + sum(map(int, str(j)))
#     if (result == N):
#         print(j)
#         break
#     if (j == N-1):
#         print(0)
#         break
#런타임 에러코드
def numSum(a):
    result = 0
    result = a + sum(map(int,str(a)))
    return result
N = int(input())
for i in range(1,N+1): # 자기자신이 분해합인 경우가 있나?
    if (N == numSum(i)):
        print(i)
        break
    if(i == N):
        print(0)
