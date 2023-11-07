import sys
n = int(input())

n_list = []
for _ in range(n) :
    n_list.append(sys.stdin.readline())

n_list.sort()

for i in range(n) :
    print(n_list[i])