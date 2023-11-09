import sys
n = int(input())

word_list = set()

for _ in range(n) :
    word_list.add(sys.stdin.readline())

word_list = list(word_list)
word_list.sort(key=lambda x : (len(x), x))

for word in word_list :
    print(word)