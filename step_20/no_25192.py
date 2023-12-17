import sys
n = int(input())

n_set = set()
result = 0
for _ in range(n):
    s = sys.stdin.readline().rstrip()

    if s == 'ENTER' :
        result += len(n_set)
        n_set = set()
    else :
        n_set.add(s)

result += len(n_set)
print(result)