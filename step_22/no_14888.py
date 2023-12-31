import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))
plus, mi, mul, div = map(int, sys.stdin.readline().rstrip().split())

maximum = -1e9
minium = 1e9

def dfs(depth, total, plus, mi, mul, div) :
    global maximum, minium
    if depth == n :
        maximum = max(total, maximum)
        minium = min(total, minium)
        return

    if plus :
        dfs(depth + 1, total + n_list[depth], plus-1, mi, mul, div)
    if mi :
        dfs(depth + 1, total - n_list[depth], plus, mi-1, mul, div)
    if mul :
        dfs(depth + 1, total * n_list[depth], plus, mi, mul-1, div)
    if div :
        dfs(depth + 1, int(total / n_list[depth]), plus, mi, mul, div-1)


dfs(1, n_list[0], plus, mi, mul, div)
print(maximum)
print(minium)