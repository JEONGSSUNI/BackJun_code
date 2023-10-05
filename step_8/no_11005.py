sip, N = map(int, input().split())
B = ""
while sip != 0 :
    if sip % N > 9 :
        B += chr((sip % N) + 55)
    else :
        B += str(sip % N)
    sip = sip // N
print(B[::-1])

# answer = ""
# sun = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# while sip != 0 :
#     answer += str(sun[sip % N])
#     sip //= N
# print(answer[::-1])