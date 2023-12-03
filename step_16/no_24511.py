import sys
from collections import deque
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split())) # 0 : 큐, 1 : 스택
b = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

queuestack = deque([])

for i in range(n) :
    if a[i] == 0 :
        queuestack.appendleft(b[i])

for i in range(m) :
    queuestack.append(c[i])
    print(queuestack.popleft(), end=' ')