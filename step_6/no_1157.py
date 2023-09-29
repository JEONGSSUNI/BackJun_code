# word = input()
#
# abc = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
# count = [0 for i in range(26)]
#
# word = word.upper()
# for s in word :
#     count[abc.find(s)] += 1
#
# max_count = max(count)
# max_list = []
# for idx in range(len(count)) :
#     if count[idx] == max_count :
#         max_list.append(idx)
#     else :
#         continue
#
# if len(max_list) == 1 :
#     print(abc[max_list[0]])
# else :
#     print('?')

# 다른 정답 풀이
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list :
    count = word.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1 :
    print("?")
else :
    print(word_list[cnt.index(max(cnt))])