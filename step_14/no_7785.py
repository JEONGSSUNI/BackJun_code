import sys
n = int(input())

member = {}
for _ in range(n) :
    name, state = sys.stdin.readline().split()
    if state == 'leave' :
        del member[name]
    else :
        member[name] = 1

member = sorted(member.keys(), reverse=True) # → member 타입이 dic에서 list로 변경됨

for name in member :
    print(name[0])