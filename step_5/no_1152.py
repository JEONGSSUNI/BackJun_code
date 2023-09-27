# 왜 틀렸다고 채점되는지 모르겠음 / if문 제외하면 정답처리 됨
string = input()

if len(string) < 1000000 :
    # split() : 공백이 n개여도 무조건 1개로 인식함
    # split(' ') : 공백 1개, 1개를 각각의 공백으로 따로따로 처리
    word = string.strip().split()
    print(len(word))
else :
    print('1000000자 이하 글자를 입력해주세요.')

# # 간단 버젼
# string = input().split()
# print(len(string))