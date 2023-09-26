n = int(input())

if 1 <= n <= 9 :
    for i in range(1, 10) :
        print(f"%d * %d = %d" %(n, i, n*i))