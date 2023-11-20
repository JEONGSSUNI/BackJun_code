import sys

def gcd(a, b) :
    while b != 0 :
        mod = a % b
        a = b
        b = mod
        return a

n = int(sys.stdin.readline())

a_distance = []
# 첫번째 나무
a = int(sys.stdin.readline())
a_distance.append(a)

each_distance = []
for i in range(n-1) :
    num = int(sys.stdin.readline())
    a_distance.append(num)
    each_distance.append(num - a) # 직전 나무와의 거리
    a = num

max_distance = each_distance[0]
for j in range(n-2) :
    max_distance = gcd(each_distance[j+1]-each_distance[j], max_distance)

result = ((a_distance[-1] - a_distance[0]) // max_distance) - n + 1
print(result)