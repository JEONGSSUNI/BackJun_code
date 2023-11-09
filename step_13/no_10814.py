import sys
n = int(input())

user_list = []
for _ in range(n) :
    age, name = sys.stdin.readline().split()
    user_list.append([int(age), name])

user_list.sort(key=lambda x : x[0])

for idx_list in user_list :
    print(idx_list[0], idx_list[1])