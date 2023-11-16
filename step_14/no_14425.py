import sys
n, m = map(int, sys.stdin.readline().split())
word = set()

for i in range(n) :
    word.add(sys.stdin.readline())

answer = 0
for _ in range(m) :
    s = sys.stdin.readline()
    if s in word :
        answer += 1

print(answer)