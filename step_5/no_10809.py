# index() : 문자열뿐만 아니라 리스트, 튜플 등 사용 가능
# find() : 문자열에서만 사용 가능

# # index() 사용
# input_str = input()
# abc = 'abcdefghijklmnopqrstuvwxyz'
# l = [-1] * 26
#
# for al in input_str :
#     # input_str.index(al) : al이 있는 위치의 인덱스 반환 (중복일 경우 첫번째 위치 반환)
#     # abc.index(al) : al이 있는 인덱스 위치 반환 = 알파벳 위치 인덱스 반환
#     # l[abc.index(al)] : 알파벳의 위치를 반환할 리스트 인덱스의 값
#     l[abc.index(al)] = input_str.index(al)
#
# for num in l :
#     print(num, end=' ')

# find() 사용
input_str = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc :
    # find() : 특정 문자를 찾으면 그 문자의 위치(첫번쨰 위치) 반환 / 못 찾으면 -1 반환
    print(input_str.find(i), end=' ')

# # 아스키 코드 사용
# input_str = input()
# check = [-1 for i in range(26)]
#
# for i in range(len(input_str)) :
#     if check[ord(input_str[i]) - 97] != -1 :
#         continue
#     else :
#         check[ord(input_str[i]) - 97] = i
#
# for i in range(26) :
#     print(check[i], end=' ')
