import json

# def set_charact(name):
def set_charact(name):
    character = {
        "닉네임" : name,
        "체력" : 50,
        "무기" : "초보자의 검",
        "방어구" : "천 갑옷",
        "공격력" : 3,
        "방어력" : 1,     
        "AA" : "평타",
        "스킬" : "파워 슬래쉬"
    } 
    with open("static/save.txt", "w", encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii = False, indent=4)
    # print("{0}님 반갑습니다." .format(character["닉네임"]))
    return character

def save_game(filename, charact):
    f = open(filename, "w", encoding='utf-8')
    for key in charact:
        print("%s:%s" % (key, charact[key]))
        f.write("%s:%s\n" % (key, charact[key]))
    f.close() 

name = input("사용하실 닉네임을 입력해 주세요: ")
print(name, "이(가) 닉네임으로 설정 되었습니다.")

# ##캐릭터 설정 함수
character = set_charact(name)

print(character)

##캐릭터 정보 파일에 저장
save_game("save.txt",character)
