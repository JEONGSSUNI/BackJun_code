while True :
    try :
        print(input())
    except EOFError :
        break

# while문을 생각하지 못함
# EOFError : End Of File(문자의 끝)
# sys.stdin.readline()은 EOF를 받을 때 빈 문자열을 리턴함 ∵ if s == "" : break로 처리해야함
# input()는 EOF를 받을 때 EOFError를 발생시킴