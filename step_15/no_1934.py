# 유클리드 호제법
def gcd(a, b) :
    if a % b == 0 :
        return b
    elif b == 0 :
        return a
    else :
        return gcd(b, a % b)

# 풀이
n = int(input())
for _ in range(n) :
    a, b = map(int, input().split())
    result = a * b
    
    while b > 0 :
        a, b = b, a % b
        
    print(result // a)