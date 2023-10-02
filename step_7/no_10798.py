word_list = []
for i in range(5):
    word_list.append(input())

for i in range(len(max(word_list, key=len))):
    for st in word_list:
        try:
            print(st[i], end='')
        except IndexError :
            continue