import sys

def gcd(a, b) :
    while b != 0 :
        mod = a % b
        a = b
        b = mod
    return a

n = int(sys.stdin.readline())

all_distance = [] # 나무의 위치
# 첫번째 나무
a = int(sys.stdin.readline())
all_distance.append(a)

each_distance = [] # 나무들 사이의 간격
for i in range(n-1) :
    num = int(sys.stdin.readline())
    all_distance.append(num)
    each_distance.append(num - a) # 직전 나무와의 거리
    a = num

max_distance = each_distance[0] # 최대 공약수
for j in range(n-2) :
    max_distance = gcd(each_distance[j+1], max_distance)

result = ((all_distance[-1] - all_distance[0]) // max_distance) - n + 1
print(result)