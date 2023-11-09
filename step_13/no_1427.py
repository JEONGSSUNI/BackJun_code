n = int(input())
num = sorted(list(map(int, str(n))), reverse=True)
for i in num :
    print(i, end='')