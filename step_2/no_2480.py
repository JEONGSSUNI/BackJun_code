a, b, c = map(int, input().split())
num = [a, b, c]

if a == b == c :
    money = 10000 + (a * 1000)
elif a == b or a == c or b == c :
    if a == b or a == c :
        money = 1000 + (a * 100)
    else :
        money = 1000 + (b * 100)
else :
    max = a
    for i in range(0, len(num)) :
        if max < num[i] :
            max = num[i]
    money = max * 100
    # money = max(a, b, c) * 100   # max함수 사용
print(money)