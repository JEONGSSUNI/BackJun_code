# 삼각형의 조건 : 최대값이 나머지 두 변의 길이 합보다 길면 안된다
# if max값이 sum(두 변)보다 길이가 길다면 최대 길이의 삼각형 = sum(두 변) + (sum(두 변) - 1)
# else sum(세 변)

x, y, z = map(int, input().split())

if max((x, y, z)) < sum((x, y, z)) - max((x, y, z)) :
    print(sum((x, y, z)))
else :
    print(2 * (sum((x, y, z)) - max((x, y, z))) - 1)

# 간단 버젼
num_list = sorted(list(map(int, input().split())))
result = num_list[0] + num_list[1] + min(num_list[2], num_list[0] + num_list[1] - 1)
print(result)