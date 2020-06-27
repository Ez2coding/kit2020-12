def login(log_ID, log_PW):
    id = 'aaa'
    pw = '1234'

    if id == log_ID and pw == log_PW:
        return True
    else:
        return False

#사용자에게 패스워드를 입력받는다.        

id = input("아이디: ")
pw = input("패스워드 : ")

if login(id, pw):
    print("로그인 성공")
else:
    print("아이디 패스워드를 확인하세요!!")