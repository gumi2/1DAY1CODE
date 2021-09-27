'''삼각형으로 자르기 스페셜 저지
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	288	150	137	53.101%
문제
볼록 다각형이 있고, 3개의 연속된 점을 선택해서 삼각형을 만든다. 그 다음이 만든 삼각형을 다각형에서 제외한다. 원래 다각형이 N개의 점이 있었다면, 이제 N-1개의 점으로 구성된 볼록 다각형이 된다.

위의 과정은 남은 다각형이 삼각형이 될 때까지 반복한다.

볼록 다각형의 점이 시계 방향순으로 주어진다. 마지막에 남은 삼각형은 여러 가지가 있을 수 있다. 이때, 가능한 넓이의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 볼록 다각형 점의 수 N (3 ≤ N ≤ 35)이 주어진다. 둘째 줄부터 N개의 줄에는 점이 시계 방향 순서대로 주어진다. 좌표는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10-9까지 허용한다.

예제 입력 1
3
1 1
2 3
3 2
예제 출력 1
1.5
예제 입력 2
4
1 1
1 2
3 3
2 1
예제 출력 2
1.5
예제 입력 3
8
1 2
1 3
2 4
3 4
4 3
4 2
3 1
2 1
예제 출력 3
3.0
예제 입력 4
7
6 2
2 1
1 2
1 4
2 6
5 6
6 5
예제 출력 4
10.0
https://www.acmicpc.net/problem/1198
'''
def triWith(x,y,a,b,c):
    result = (x[a]*y[b]+x[b]*y[c]+x[c]*y[a])-(x[b]*y[a]+x[c]*y[b]+x[a]*y[c])
    result = abs(result)
    return result/2
N = int(input())
x = []
y = []
p = []
for i in range(N):
    p = list(map(int,input().split()))
    x.append(p[0])
    y.append(p[1])
min = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(i+2,N):
            if(min<triWith(x,y,i,j,k)):
                min = triWith(x,y,i,j,k)
print(min)
