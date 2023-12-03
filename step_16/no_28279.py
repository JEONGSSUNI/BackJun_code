import sys
from collections import deque
n = int(sys.stdin.readline())

que = deque([])

for _ in range(n) :
    s = sys.stdin.readline().split()
    s[0] = int(s[0])
    if s[0] == 1 :
        que.appendleft(int(s[1]))
    elif s[0] == 2 :
        que.append(s[1])
    elif s[0] == 3 :
        if que :
            print(que.popleft())
        else :
            print(-1)
    elif s[0] == 4 :
        if que :
            print(que.pop())
        else :
            print(-1)
    elif s[0] == 5 :
        print(len(que))
    elif s[0] == 6 :
        if que :
            print(0)
        else :
            print(1)
    elif s[0] == 7 :
        if que :
            print(que[0])
        else :
            print(-1)
    else :
        if que:
            print(que[-1])
        else:
            print(-1)