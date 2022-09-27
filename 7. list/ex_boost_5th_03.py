# Q3. 숫자 맞추기 게임을 만들어 볼게요. 컴퓨터가 임의의 숫자를 3개 만들고 우리가 그것을 맞춰보겠습니다.
# 😲조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
# 😲조건2 - 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
# 😲조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.
import random

def guess_numbers():
    random_numbers = [] # 랜덤으로 값을 얻어 작은 순으로 정렬합니다. 
    while len(random_numbers) < 3:
        number = random.randint(0, 100)
        if number in random_numbers: # 같은 수가 나올 경우 다시 값을 얻도록합니다. 
            continue
        random_numbers.append(number)
    random_numbers.sort() # 작은 순으로 정렬합니다. 
    # print(random_numbers)

    seq = 1 # 차수를 도출하기 위한 변수
    answer_check = [] # 이미 입력했던 수를 필터링하기 위한 리스트입니다. 
    while True:
        print()
        print(f"{seq}차 시도")
        input_number = input("숫자를 예측해보세요!: ")
        try: # 예외는 정수입력여부와 0과 100사이의 수인지 그리고 입력했던 수인지 확인합니다. 
            player_number = int(input_number)
            if player_number not in range(101):
                raise Exception("0과 100사이의 정수만 입력 가능합니다.")
            if player_number in answer_check:
                raise Exception("이미 예측에 사용한 숫자입니다.")
            answer_check.append(player_number)
        except Exception as e:
            print("잘못입력했습니다.", e)
            continue

        value_string = ["최솟값", "중간값", "최대값"]

        if player_number in random_numbers:
            print("잘 맞추셨습니다.")
            print(f"{player_number}는 {value_string[random_numbers.index(player_number)]}입니다!") # 랜덤값을 최솟값 중간값 최대값으로 정렬했기 때문에 그 인덱스 값으로 답변을 출력합니다. 
            print(f"{seq}차 시도만에 성공!")
            print("게임종료")
            break
        else:
            print(f"{player_number}는 없습니다.")
            if seq > 10: # 11번째 시도부터 값에 대한 힌트가 주어집니다. 
                if player_number < random_numbers[0]:
                    print(f"{player_number}는 {value_string[0]}보다 작습니다.")
                elif player_number < random_numbers[1]:
                    print(f"{player_number}는 {value_string[0]}과 {value_string[1]}사이 입니다.")
                elif player_number < random_numbers[2]:
                    print(f"{player_number}는 {value_string[1]}과 {value_string[2]}사이 입니다.")
                elif player_number > random_numbers[2]:
                    print(f"{player_number}는 {value_string[2]}보다 큽니다.")
            seq += 1

guess_numbers()
