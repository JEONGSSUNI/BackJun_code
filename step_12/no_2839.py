# 무조건 5로 나누고 3으로 나누면 안됨
# if n == 6인 경우 5로 나누면 1이 남아서 3으로 안나눠지므로 -1을 출력하게됨
# 하지만 6은 3으로 나누면 2개로 담을 수 있음
# 이런 예외 상황 전부 포함해야함

# mod이용하는 것은 안됨 → 11인 경우 5 + 6이 될 수 있음

n = int(input())
count = 0

# if (n % 5) % 3 == 0 :
#     count += n // 5
#     count += (n % 5) // 3
# elif n % 5 == 0 or n % 3 == 0 :
#     if n % 5 == 0 :
#         count += n // 5
#     else :
#         count += n // 3
# else :
#     count = -1

while n >= 0 :
    # 최소한의 봉지 개수가 목표
    # 5의 배수인 수가 될때까지 3을 빼주면서 봉지를 count한다
    # 5의 배수가 됐을 떄 5로 나눈 봉지의 개수를 count하고 print함
    if n % 5 == 0 :
        count += n // 5
        print(count)
        break

    n -= 3
    count += 1

else :
    # 3, 5로 나누어 떨어지면 while문 안에서 print 되고 while문을 빠져나옴
    # 즉 3, 5로 나누어지지 않을 경우 -1 출력
    print(-1)