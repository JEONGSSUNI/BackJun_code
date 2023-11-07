import sys
n = int(input())

n_list = []

for _ in range(n) :
    # for문 안에서 input()은 느림
    # sys.stdin.readline()으로 입력 받음
    n_list.append(int(sys.stdin.readline()))

n_list.sort()
for i in range(n) :
    print(n_list[i])