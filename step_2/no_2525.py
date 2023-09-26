h, m = map(int, input().split())
cook = int(input())

if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= cook <= 1000:
    if m + cook >= 60 :
        plus_h = (m + cook) // 60
        copy_m = (m + cook) % 60
        if h + plus_h > 23 :
            copy_h = h + plus_h - 24
        else :
            copy_h = h + plus_h
    else :
        copy_m = m + cook
        copy_h = h
    print(copy_h, copy_m)
else :
    print("24시간 기준으로 입력해주세요.")