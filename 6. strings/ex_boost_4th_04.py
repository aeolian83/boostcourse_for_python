# Q4.주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다. 주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.
# - 주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
# - 뒷자리는 1,3 은 남자 2,4는 여자
# - 00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
# - 뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음

a = "830427-1256765"
b = "031223-3456734"

def check_id(numbers):
    try:
        len(numbers) == 14
        numbers[6] == "-"
    except:
        print("잘못입력했습니다. 000000-0000000 형식으로 입력바랍니다.")
    birth_year = int(numbers[:2])
    birth_month = int(numbers[2:4])
    birth_day = int(numbers[4:6])
    gender_number = int(numbers[7])
    
    print(birth_year)
    if gender_number == 1 or gender_number == 3:
        gender = "남자"
    if gender_number == 2 or gender_number == 4:
        gender = "여자"
    if birth_year >= 0 and birth_year <= 21:
        birth_check = input("2000년 이후 출생자입니까?(맞으면 o, 틀리면 x): ")
        while True:
            try:
                birth_check == "o" or birth_check == "x"
                break
            except:
                print("잘못 입력했습니다. 다시 입력해주세요")
                continue
        if birth_check == "o" and (gender_number == 3 or gender_number == 4):
            print(f"{birth_year}년 {birth_month}월 출생 {gender}")
        elif birth_check == "o" and (gender_number == 1 or gender_number == 2):
            print("""잘못입력햇습니다.
올바른 번호를 넣어주세요""")
        elif birth_check == "x" and (gender_number == 1 or gender_number == 2):
            print(f"{birth_year}년 {birth_month}월 출생 {gender}")
        else:
            print("""잘못입력햇습니다.
올바른 번호를 넣어주세요""")
    else:
        print(f"{birth_year}년 {birth_month}월 출생 {gender}")

check_id(a)
check_id(b)

