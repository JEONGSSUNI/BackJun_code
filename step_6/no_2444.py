n = int(input())

for i in range(0, n) :
    star = "*" * ((i * 2) + 1)
    # print(star.center(n * 2))
    print(" " * (n - i - 1) + star)

for i in range(n-1, 0, -1) :
    star = "*" * ((i * 2) - 1)
    # print(star.center(n * 2))
    print(" " * (n - i) + star)