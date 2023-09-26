import sys

data_list = []
while True :
    a, b = map(int, sys.stdin.readline().split())

    if a == b == 0 :
        break
    else :
        data_list.append(a + b)

for num in data_list :
    print(num)