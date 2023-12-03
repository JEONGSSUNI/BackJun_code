import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
que = deque([i for i in range(1, n+1)])

res = []
while len(que) != 0 :
    for _ in range(k-1) :
        que.append(que.popleft())
    res.append(str(que.popleft()))

print('<' + ', '.join(res) + '>')