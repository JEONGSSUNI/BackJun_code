import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
n_list = sorted(set(num))

n_dic = {n_list[i] : i for i in range(len(n_list))}

for i in num :
    print(n_dic[i], end=' ')