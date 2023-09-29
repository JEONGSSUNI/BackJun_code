word = input()

abc = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
count = [0 for i in range(26)]

word = word.upper()

for s in word :
    count[abc.find(s)] += 1

max_count = max(count)
print(max_count)
max_list = []
for idx in range(len(count)) :
    if count[idx] == max_count :
        max_list.append(idx)
    else :
        continue

if len(max_list) == 1 :
    print(abc[max_list[0]])
else :
    print('?')