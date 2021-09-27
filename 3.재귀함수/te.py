# import sys
# N=int(sys.stdin.readline())
# L=[]
# for i in range(N):
#     L+=[[i for i in sys.stdin.readline()]]
# def f(X,Y,s):
#     n=L[X][Y]
#     for x in range(X,X+s):
#         for y in range(Y,Y+s):
#             if n!=L[x][y]:
#                 s//=2 # s = s//2
#                 return '('+f(X,Y,s)+f(X,Y+s,s)+f(X+s,Y,s)+f(X+s,Y+s,s)+')'
#     return n
# print(f(0,0,N))

#애네가 좌표가아님 !
N = int(input())
L = []
for i in range(N):
    L += [i for i in input()] #하나만 씌우면은 그대로 합쳐져서 감싼다음 더하기위해서두번함.
print(L)
