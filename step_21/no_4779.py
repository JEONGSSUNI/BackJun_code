def cut(n) :
    if n == 1 :
        return '-'
    else :
        left = cut(n // 3)
        center = ' ' * (n // 3)
        return left + center + left


import sys
while True :
    try :
        n = int(sys.stdin.readline())
        result = cut(3 ** n)
        print(result)
    except :
        break