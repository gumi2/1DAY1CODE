'''
유레카 이론 출처다국어
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	9044	5387	4208	58.952%
문제
삼각수 Tn(n ≥ 1)는 [그림]에서와 같이 기하학적으로 일정한 모양의 규칙을 갖는 점들의 모음으로 표현될 수 있다.



[그림]

자연수 n에 대해 n ≥ 1의 삼각수Tn는 명백한 공식이 있다.

Tn = 1 + 2 + 3 + ... + n = n(n+1)/2

1796년, 가우스는 모든 자연수가 최대 3개의 삼각수의 합으로 표현될 수 있다고 증명하였다. 예를 들어,

4 = T1 + T2
5 = T1 + T1 + T2
6 = T2 + T2 or 6 = T3
10 = T1 + T2 + T3 or 10 = T4
이 결과는 증명을 기념하기 위해 그의 다이어리에 “Eureka! num = Δ + Δ + Δ” 라고 적은것에서 유레카 이론으로 알려졌다. 꿍은 몇몇 자연수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 궁금해졌다. 위의 예시에서, 5와 10은 정확히 3개의 삼각수의 합으로 표현될 수 있지만 4와 6은 그렇지 않다.

자연수가 주어졌을 때, 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 없는지를 판단해주는 프로그램을 만들어라. 단, 3개의 삼각수가 모두 달라야 할 필요는 없다.

입력
프로그램은 표준입력을 사용한다. 테스트케이스의 개수는 입력의 첫 번째 줄에 주어진다. 각 테스트케이스는 한 줄에 자연수 K (3 ≤ K ≤ 1,000)가 하나씩 포함되어있는 T개의 라인으로 구성되어있다.

출력
프로그램은 표준출력을 사용한다. 각 테스트케이스에대해 정확히 한 라인을 출력한다. 만약 K가 정확히 3개의 삼각수의 합으로 표현될수 있다면 1을, 그렇지 않다면 0을 출력한다.
https://www.acmicpc.net/problem/10448
'''
N = 44 #1000 보다 가장 작은 tlist의 개수
tlist = [int(i*(i+1)/2) for i in range (1, 45)]
print(tlist[::-1])
result = int(input())
cnt = 0
double = 'a'
triple = 'a'
for i in range(len(tlist)):
    if tlist[::-1][i] < result:
        result -= tlist[::-1][i]
        cnt += 1
    if double == 'b':
        break
    if triple == 'b':
        break
    for j in range(len(tlist)):
        if tlist[::-1][j] <= result:
            cnt += 1
            result -= tlist[::-1][j]
        if result == 0:
            double = 'b'
            break
        if triple == 'b':
            break
        for k in range(len(tlist)):
            if tlist[::-1][k] <= result and cnt != 0:
                cnt += 1
                result -= tlist[::-1][k]
                print('결과값{0}'.format(result))
                break
            if tlist[::-1][k] < result:
                cnt += 1
                result -= tlist[::-1][k]
                print('결과값{0}'.format(result))
                break
            if result == 0 or cnt>=3:
                triple = 'b'
                break
print(cnt)
if cnt == 3 and result ==0:
    print(1)
else:
    print(0)
# 뭔가 애매하다
