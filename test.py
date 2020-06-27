import time,random




def charact(name,weapons,Amor,Dmg,Def):
    status = {
        "닉네임" : name,
        "체력" : 100,
        "무기" : Weapons,
        "방어구" : Amor,
        "공격력" : Dmg,
        "방어력" : Def     
    }          





def game():
    time.sleep(1) 
    print ("길을 가다 도적들을 만났습니다.\n1.싸운다\n2.도망친다")
    act1 = int(input("번호로 선택:"))

    if  act1 ==1:
        print ("용기는 가상했지만 도적들이 너무 강해 사망하셨습니다.\nTo be continued")
    elif act1 == 2: 
        print("적에게 등을 보여 화살에 맞아 죽었습니다.\nThe End")
    else:  
        print("잘못 입력하셨습니다. 숫자를 입력해주세요 ")
        return game()   





    
# name = input("사용하실 닉네임을 입력해 주세요: ")
# dictionary["닉네임"] = name
# print(name, "이(가) 닉네임으로 설정 되었습니다.") 

def ID_check():

 log_ID = "aaa"
 log_PW = "1234"
 id = str(input("ID를 입력하시오: "))
 pw = input("패스워드를 입력하시오: ")
    
 if log_ID == id and log_PW == pw:

     


    with open("userInfo.txt", "w", encoding = "utf-8") as file:
        # file.write(id + "," + pw + "," + name + '\n') 
        file.write(id + "," + pw + '\n')

    with open("userInfo.txt", "r", encoding= "utf-8") as file:
     for line in file:
         try:
            (id, pw, name) = line.strip().split(",")
            # (id, pw) = line.strip().split(",")
            print("\n".join([
            "아이디: {}",
            "비밀번호: {}" #,
            # "닉네임: {}"
            # ]).format(id, pw, name))
            ]).format(id, pw))
            print()       
         except:
             pass    
 else:
    print("잘 못 입력하셨습니다.")        
    return ID_check()
    start = ID_check()
print(ID_check())

name = input("사용하실 닉네임을 입력해 주세요: ")
print(name, "이(가) 닉네임으로 설정 되었습니다.")

# print ("{0}님 반갑습니다. 장비를 선택하세요." .format(dictionary["닉네임"]))
# print ("{0}님 반갑습니다. (체력 {1})으로 게임을 시작 합니다." .format(dictionary["닉네임"], dictionary["체력"]))
          



def ChoiceW():
     
    print("1.검 2.방패 3.활 4.??? 중에 무기를 선택하시오.")

    choice = int(input("번호를 입력하세요.: "))



    if choice == 1: 
            Weapons = "초보자의 검"
            Dmg = "3"
            # dictionary["무기"] = "초보자의 목검"
            # dictionary["공격력"] = "2"
            print (Weapons, "이 지급되었습니다. ")
            # print (dictionary["name"],"님이 검을 가지고 여행을 떠납니다.")
            
      
    elif choice ==2:
            Weapons = "초보자의 단검"
            Dmg = "1"
            print (Weapons, "이 지급되었습니다. ")
        # dictionary["무기"] = "나무 방패"
        # dictionary["공격력"] = "0"
        # print (dictionary["무기"], "가 지급되었습니다.")
        # print (dictionary["name"], "님이 방패를 가지고 여행을 떠납니다.")
        
    elif choice == 3:
        Weapons = "초보자의 활"
        Dmg = "4"
        print (Weapons, "이 지급되었습니다. ")
        # dictionary["무기"] = "초보자의 활"
        # dictionary["공격력"] = "4"
        # print (dictionary["무기"],"이 지급되었습니다.")
        # print (dictionary["name"],"님이 활을 가지고 여행을 떠납니다.")
        
    elif choice == 4:
        Weapons = "맨손"
        Dmg = "1"
        print (Weapons, "이 지급되었습니다. ")
        # dictionary["무기"] = "원펀치 주먹"
        # dictionary["데미지"] = "9999"
        # print ("축하합니다. 당신은 이미", dictionary["무기"],"이 지급되었습니다.")
        # print (dictionary["name"],"님이 원펀치 주먹 으로 여행을 떠납니다.")
    else:
        print("잘못입력하셨습니다. 다시 확인해주세요")
        return ChoiceW()
ChoiceW()

    

def choiceA():
    print("방어구를 선택하시오 1.가죽 조끼 2.천 갑옷 3. 풀 플레이트 아머")

    choice = int(input("번호를 입력하세요.: "))

    if choice == 1:
        Amor = "가죽조끼"
        Def = "3"
        print(Amor, "(이)가 지급되었습니다. ")
    
        # dictionary["방어구"] = "가죽 조끼"
        # dictionary["방어력"] = "3"
        # print(dictionary["방어구"],"가 지급 되었습니다.")
    elif choice == 2: 
        Amor = "천 갑옷"
        Def = "1"
        print(Amor, "(이)가 지급되었습니다. ")
        # dictionary["방어구"] = "천 갑옷"
        # dictionary["방어력"] = "0"
        # print(dictionary["방어구"],"이 지급 되었습니다.")
    elif choice == 3: 
        Amor = "더러워진 나시"
        Def = "0"
        print(Amor, "(이)가 지급되었습니다. ")
        # dictionary["방어구"] = "없음"
        # dictionary["방어력"] = "0"
        # print(dictionary["방어구"],"가 너무 무거워 입지 못합니다.")
    else: 
        print("잘못입력하셨습니다. 다시 확인해주세요")     
choiceA()

print(charact(name,weapons,Amor,Dmg,Def))




f = open("save.txt", "w", encoding="utf-8")
for key in dictionary:
    print("%s:%s" % (key, dictionary[key]))
    f.write("%s:%s\n" % (key, dictionary[key]))
f.close()    


# def charact(name):
#     character = {
#         "level" : 1,
#         "hp": 100,
# }
#     print ("{0}님 반갑습니다. (체력 {1})으로 게임을 시작 합니다." .format(character["name"], character["hp"]))
#     return character





game()
      


