import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n) :
    x = sys.stdin.readline()

    if len(x) > 2 :
        stack.append(int(x[2:]))
    elif int(x) == 2 :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif int(x) == 3 :
        print(len(stack))
    elif int(x) == 4 :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    else :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])