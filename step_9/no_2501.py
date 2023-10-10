facotor_list = []
n, k = map(int, input().split())
count = 1
while n >= count :
    if n % count == 0 :
        facotor_list.append(count)
    count += 1

if len(facotor_list) >= k :
    print(facotor_list[k-1])
else :
    print(0)