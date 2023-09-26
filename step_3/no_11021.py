import sys
n = int(input())
sum_list = []
for i in range(0, n) :
    a, b = map(int, sys.stdin.readline().split())
    sum_list.append(a + b)

for num in range(len(sum_list)) :
    print("Case #%d: %d" %(num + 1, sum_list[num]))