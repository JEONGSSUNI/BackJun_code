def append_star(n) :
    if n == 1 :
        return ['*']

    stars = append_star(n // 3)

    L = []

    for S in stars :
        L.append(S * 3)
    for S in stars :
        L.append(S + ' ' * (n // 3) + S)
    for S in stars:
        L.append(S * 3)
    return L

import sys
n = int(sys.stdin.readline())
print('\n'.join(append_star(n)))