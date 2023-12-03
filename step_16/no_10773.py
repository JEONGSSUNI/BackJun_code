import sys
k = int(sys.stdin.readline())

result = []
for _ in range(k) :
    x = int(sys.stdin.readline())
    if x == 0 :
        result.pop()
    else :
        result.append(x)

print(sum(result))