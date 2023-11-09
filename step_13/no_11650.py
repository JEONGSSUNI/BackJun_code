import sys
n = int(input())

point_list = []

for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    point_list.append([x, y])

point_list.sort(key=lambda x : (x[0], x[1]))

for i in range(n) :
    print(point_list[i][0], point_list[i][1])