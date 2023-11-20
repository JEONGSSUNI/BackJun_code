a, b = map(int, input().split())
result = a * b
while b > 0 :
    # print(a % b)
    a, b = b, a % b
print(result // a)