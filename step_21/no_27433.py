import sys
# sys.setrecursionlimit(1**6)

def fac(x) :
    if x == 1 :
        return x
    elif x == 0 :
        return 1
    else :
        return x * fac(x-1)

n = int(sys.stdin.readline())
print(fac(n))