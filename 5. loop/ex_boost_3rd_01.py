# Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.
# 조건 1: 홀 수 번째만 출력하기
# 조건 2: 값이 50이하인 것만 출력하기

def int_input():
    while True:
        number = input("몇 단?: ")
        try:
            number = int(number)
            return number
        except:
            print("잘못 입력했습니다. 정수만 입력 가능합니다.")
            continue
        
def gugudan(number):
    print(number, "단")
    for i in range(1, 10):
        result = number * i
        if i % 2 == 0:
            continue
        if result > 50:
            break
        print(number," X ",i, " = ",result)
    return

number = int_input()

gugudan(number)