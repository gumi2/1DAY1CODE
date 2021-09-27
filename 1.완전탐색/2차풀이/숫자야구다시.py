import sys
from itertools import permutations
n = [i for i in range(1,10)]
num = list(permutations(n,3))

t = int(sys.stdin.readline())
for _ in range(t):
    test, s, b  = map(int,sys.stdin.readline().split())
    test = list(str(test)) # 자리수로 움직일꺼면 str 해주는게 편함
    rv_cnt = 0
    for i in range(len(num)):
        s_c = b_c = 0
        i -= rv_cnt
        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i]:
                if j == num[i].index(test[j]):
                    s_c += 1
                else:
                    b_c += 1
        if s_c != s or b_c != b:
            num.remove(num[i])
            rv_cnt +=1
print(len(num))
