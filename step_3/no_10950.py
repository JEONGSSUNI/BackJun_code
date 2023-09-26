test_n = int(input())
plus_list = []

for i in range(test_n) :
    a, b = map(int, input().split())
    plus_list.append(a + b)
    # plus_list.append([a, b])

for num in plus_list :
    print(num)

# for a, b in plus_list :
#     print(a + b)
