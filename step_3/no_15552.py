import sys

n = int(input())
plus_list = []
for i in range(0, n) :
    a, b = map(int, sys.stdin.readline().split())
    plus_list.append(a + b)

for num in plus_list :
    print(num)