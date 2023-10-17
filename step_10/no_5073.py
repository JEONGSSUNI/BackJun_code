result_list = []
while True :
    # length = []
    x, y, z = map(int, input().split())
    # length.append(x)
    # length.append(y)
    # length.append(z)

    if x == 0 and y == 0 and z == 0 :
        break

    # max_data = max(length)
    # length.remove(max_data)

    # if max_data < sum(length) :
    # max 제외한 두 변의 합 구하는 방법 : sum - max를 생각하지 못 함
    if max((x, y, z)) < sum((x, y, z)) - max((x, y, z)):
        # length.append(max_data)
        # if len(set(length)) == 1 :
        if len(set((x, y, z))) == 1 :
            result_list.append('Equilateral')
        # elif len(set(length)) == 2 :
        elif len(set((x, y, z))) == 2 :
            result_list.append('Isosceles')
        else :
            result_list.append('Scalene')
    else :
        result_list.append('Invalid')

for data in result_list :
    print(data)