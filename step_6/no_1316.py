# # len(word)) : 다음 문자와 비교해야하므로 길이보다 1개 적게 for문 돌려야함
# # word의 글자 한개 한개를 담으려고 word_list를 set으로 만들었으나 그렇게 비교하면 연속으로 중복되는 순간 -1이 됨
# # error
# n = int(input())
# count = n
# for i in range(n) :
#     word = input()
#     word_list = set()
#     for s in range(len(word)-1) :
#         if word[s] == word[s+1] :
#             word_list.add(word[s])
#         elif word[s] in word_list :
#             count -= 1
#         else :
#             word_list.add(word[s])
# print(count)

# 풀이 참고
n = int(input())
count = n

for i in range(n) :
    word = input()
    for s in range(len(word)-1) :
        if word[s] == word[s+1] :
            continue
        # word[s]가 word[s+1:]에 있는지 확인
        # if에서 연속이면 continue이기에 연속 이후에 같은 글자가 있는지 확인
        # 연속 이후에 같은 글자가 있으면 그룹 단어가 아니므로 -1하고 break해야함 안하면 -1이상이 될 수 있음
        elif word[s] in word[s+1:] :
            count -= 1
            break
print(count)