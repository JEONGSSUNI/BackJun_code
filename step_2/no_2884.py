h, m = map(int, input().split())

if 0 <= h <= 23 and 0 <= m <= 59 :
    if m < 45 :
        am = m + 15
        if h == 0 :
            ah = 23
        else :
            ah = h - 1
    else :
        am = m -45
        ah = h
    print(ah, am)
else :
    print("24시간 기준으로 입력해주세요.")