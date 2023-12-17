import sys
n, m = map(int, sys.stdin.readline().split())
word_list = {}

for _ in range(n) :
    word = sys.stdin.readline().rstrip()

    if len(word) < m :
        continue
    else :
        if word in word_list :
            word_list[word] += 1
        else :
            word_list[word] = 1

# x[1] = 단어 횟수, x[0] = 단어
# -x[1] = 단어가 많이 나온 기준, -len(x[0]) = 단어의 길이가 긴 순서
word_list = sorted(word_list.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for w in word_list :
    print(w[0])