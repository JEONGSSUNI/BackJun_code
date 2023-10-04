B, N = input().split()
N = int(N)
total_10 = 0
for i in range(0, len(B)) :
    try :
        x = int(B[len(B) - (i+1)])
    except ValueError :
        x = ord(B[len(B) - (i+1)]) - 55
    total_10 += (N ** i) * x
print(total_10)