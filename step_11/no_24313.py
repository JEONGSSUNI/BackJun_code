a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# a1 <= c를 해야하는 이유
# : c가 a1보다 크거나 같으면 음수가 있든 말든 보장 해주기 때문
# ex) a0가 음수일 경우 / 4n - 2 <= 2n 에서 1일때는 성립하지만 2일때는 성립하지 않음

if ((a1 * n0) + a0 <= c * n0) and a1 <= c :
    print(1)
else :
    print(0)