test_n = int(input())
test_case = []
for i in range(test_n) :
    test_case.append(str(input()))

for test_str in test_case :
    first_last = test_str[0] + test_str[-1]
    print(first_last)
    # 출력할 때 ,로 구분하면 공백 있음 / +로 하면 공백없이 출력
    
# strip() : 양 끝의 불필요한 문자를 삭제
# replace() : 지정 문자열을 치환하여 삭제
# translate() : 여러 개로 지정한 문자열을 한 번에 삭제 / 가장 빠름
# import re
# re.sub() : 복잡한 패턴의 문자열을 치환하여 삭제