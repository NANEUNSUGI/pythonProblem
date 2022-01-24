import random

computer = random.randint(0,2)
user = int(input("하나를 선택하세요 : 가위(0), 바위(1), 보(2) : "))

def game(a,b):
    if a == b:
        return "비겼습니다"
    else:
        if a==0:
            if b==1:
                return "졌습니다"
            else:
                return "이겼습니다"
        elif a==1:
            if b==0:
                return "이겼습니다"
            else:
                return "졌습니다"
        elif a==2:
            if b==1:
                return "이겼습니다"
            else:
                return "졌습니다"


print(game(computer,user))