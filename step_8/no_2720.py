# 쿼터 0.25 / 다임 0.10 / 니켈 0.05 / 페니 0.01
# 25 / 10 / 5 / 1
n = int(input())
test = []
for i in range(n) :
    i_test = []
    jandon = int(input())

    i_test.append(jandon // 25)
    jandon %= 25

    i_test.append(jandon // 10)
    jandon %= 10

    i_test.append(jandon // 5)
    i_test.append(jandon % 5)
    test.append(i_test)

for i in test :
    for j in i :
        print(j, end=' ')
    print()


# 간단하게 작성
for _ in range(n) :
    money = int(input())
    for i in [25, 10, 5, 1] :
        print(money // i, end=' ')
        money = money % i