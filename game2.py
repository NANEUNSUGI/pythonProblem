import random

com = random.randint(1,99)

count = 0
while True:

    count += 1
    print(f"시도 횟수는{count}번입니다. ")
    user = int(input('숫자를 입력하세요. '))

    if user > com:
        print('다운')
    elif user < com:
        print('업')
    else:
        print('정답입니다.!!!!')
        break