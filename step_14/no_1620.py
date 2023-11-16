import sys
n, m = map(int, sys.stdin.readline().split())

poketmon = {}
for i in range(1, n+1) :
    # poketmon[i] = (sys.stdin.readline()).splitlines()[0]
    poketmon[i] = sys.stdin.readline().rstrip()

reverse_poketmon = dict(map(reversed, poketmon.items()))

for _ in range(m) :
    # ip = (sys.stdin.readline()).splitlines()[0]
    ip = sys.stdin.readline().rstrip()

    # try, except 활용
    try :
        int(ip)
    except ValueError :
        print(reverse_poketmon[ip])
    else :
        print(poketmon[int(ip)])

    # # if문 활용
    # if ip.isdigit() : # int형인지 확인하는 함수를 생각하지 못함
    #     print(poketmon[int(ip)])
    # else :
    #     print(reverse_poketmon[ip])