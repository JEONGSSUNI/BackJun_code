total = int(input())
n = int(input())
price = []
for i in range(n) :
    money, num = map(int, input().split())
    price.append(money * num)

sum = 0
for i in price :
    sum += i

if total == sum :
    print('Yes')
else :
    print('No')