import sys
n = int(sys.stdin.readline())

rainbow = {'ChongChong'}
for _ in range(n) :
    a, b = sys.stdin.readline().split()

    if a in rainbow:
        rainbow.add(b)

    if b in rainbow :
        rainbow.add(a)

print(len(rainbow))