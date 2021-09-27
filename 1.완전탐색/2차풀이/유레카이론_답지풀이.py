import itertools
def tri(num):
    return num*(num+1)/2
N = int(input())
a = [int(input()) for i in range(N)]
t = []
for i in a:

    j = 1
    while tri(j)<=i:
        t.append(tri(j))
        j +=1
    tl = list(itertools.combinations_with_replacement(t,3))
    cnt = 0
    for k in tl:
        if sum(k) == i:
            print(1)
            break
        else:
            cnt += 1
        if cnt == len(tl):
            print(0)
            break
