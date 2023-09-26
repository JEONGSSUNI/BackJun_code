import sys
n = int(input())
data_list = []
for i in range(n) :
    data_list.append(list(map(int, sys.stdin.readline().split())))

for d in range(0, len(data_list)) :
    print("Case #%d: %d + %d = %d" %(d + 1, data_list[d][0], data_list[d][1], data_list[d][0] + data_list[d][1]))