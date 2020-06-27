

def character(name, Weapons,Amor):
    info = {
        "닉네임" : name,
        "체력": 100,
        "무기" : Weapons,
        "방어구" : Amor   
    }        
    print("{0}님 반갑습니다." .format(info["닉네임"]))
    return info
    
name = input("사용할 닉네임을 입력하세요: ")


def choice():

    print("1.검 2.방패 3.활 4.??? 중에 무기를 선택하시오.")
    Weapons = int(input("번호를 입력하세요.: "))

    if Weapons == 1: 
        Weapons = "초보자의 검"
    elif Weapons ==2:
        Weapons = "초보자의 단검"
    elif Weapons == 3:
        Weapons = "초보자의 활"
    elif Weapons == 4:
        Weapons = "맨손"
    else:
        print("잘못입력하셨습니다. 다시 확인해주세요")
        return choice()
    print(Weapons,"을 획득하셨습니다.")    
    
    print("방어구를 선택하시오 1.가죽 조끼 2.천 갑옷 3. 풀 플레이트 아머")
    Amor = int(input("번호를 입력하세요.: "))
    if Amor == 1:
        Amor = "천 갑옷"
    elif Amor == 2:
        Amor = "가죽 갑옷"
    elif Amor == 3:
        Amor = "사슬 갑옷"
    else:
        print("잘못입력하셨습니다. 다시 확인해주세요")
        return choice()
    print(Amor, "(을)를 획득하셨습니다.")

    status = character(name,Weapons,Amor)
    print(status)
choice()


    


