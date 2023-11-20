def gcd(a, b) :
    while a % b != 0 :
        mod = a % b
        a = b
        b = mod
    return b

a, n = map(int, input().split())
b, m = map(int, input().split())

son = (a * m) + (b * n)
parant = n * m

n = gcd(son, parant)

print(son//n, parant//n)