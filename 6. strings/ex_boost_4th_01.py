# Q1. 우리는 큰 수를 나타낼 때 3자리마다 , 를 찍어서 구분해 줍니다. 파이썬에서는 아래와 같이 쉽게 나타낼 수 있습니다.
# 하지만 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는 함수를 만들어 봅시다.

print(f"{1000:,}")
print(f"{230601000:,}")

def make_comma(number):
    print(f"{number:,}")

def int_input():
    while True:
        number = input("숫자를 입력하세요: ")
        try:
            number = int(number)
            return number
        except:
            print("잘못 입력했습니다. 정수만 입력 가능합니다.")
            continue

number = int_input()
make_comma(number)

