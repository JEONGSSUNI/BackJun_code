have = list(map(int, input().split()))
can_play = [1, 1, 2, 2, 2, 8]

need = [0 for i in range(len(have))]

for i in range(len(have)) :
    # if have[i] >= can_play[i] :
    #     need[i] = can_play[i] - have[i]
    # else :
    #     need[i] = can_play[i] - have[i]

    # if, else문의 식이 같으므로 한 줄만 적어도 됨
    need[i] = can_play[i] - have[i]

for i in need :
    print(i, end=' ')