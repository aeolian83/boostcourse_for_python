# Q1. 여러분 혹시 베스킨라빈스31 게임을 아시나요? 1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가 31을 외치는 사람이 패배하는 게임인데요.
# - 이번엔 이 게임을 파이썬 함수로 만들어 봅시다. 지성이 없이 숫자를 랜덤하게 외치는 컴퓨터와 대결을 해보겠습니다.
# 😲조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분
# 😲조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음
# 😲조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)

import random

def baskin_game(): # 게임은 각각 컴퓨터와 사람이 부른 숫자를 리스트에 입력해서 리스트의 길이가 31이 넘는 순간 게임이 종료되며 31을 외쳤을 때 외친자가 패합니다.
    game_list = [] # 편이를 위하여 컴퓨터가 먼저 플레이를 시작합니다.
    computer_play = random.randint(1,3)
    for i in range(computer_play):  # 랜덤으로 생성된 수만큼 리스트에 주를 더합니다. 
        game_list.append(i+1)
    print(f"현재 배스킨라빈스는 {game_list}까지 만들어졌습니다.")

    while True:
        my = input("My turn - 숫자를 입력하세요: ")
        try:
            player_num = my.split()  # 띄어쓰기로 각 수를 구문하는 만큼 띄어쓰기를 기준으로 수를 리스트로 만듭니다. 
            player_num = list(map(int, player_num)) # input으로 입력을 받을때는 str로 만들어지기 때문에 int로 데이터 형태를 변형합니다.
            if len(player_num) > 3: # 배스킨 게임은 숫자를 3개까지만 외칠수 있기 때문에 3개를 초과해서 썼는지 확인합니다. 
                raise Exception("연속된 정수 3개까지만 입력 가능합니다.")
            if player_num[0] != game_list[-1] + 1: # 컴퓨터가 부른 수의 바로 연속된 다음수를 썼는지 확인합니다. 
                raise Exception("컴퓨터가 부른 숫자의 연속된 다음 수를 입력하십시오.")
            for i in range(1, len(player_num)): # 입력된 정수가 연속된 3개의 정수인지 확인합니다.
                if player_num[i] != (player_num[i - 1]) + 1:
                    raise Exception("연속된 다음 수를 입력하십시오.")
        except Exception as e:
            print("다시 입력하시오.", e)
            continue

        game_list.extend(player_num) # 플레이어가 입력한 부분을 리스트네 추가합니다. 
        if len(game_list) >= 31:
            print("Player가 패배했습니다.")
            break

        computer_play = random.randint(1,3)
        for i in range(computer_play):
            game_list.append(game_list[-1] + 1)
        print(f"컴퓨터는 {game_list[0 - computer_play:]}을 불렀습니다")
        if len(game_list) >= 31:
            print("Computer가 패배했습니다.")
            break
        print(f"현재 배스킨라빈스는 {game_list}까지 만들어졌습니다.")

baskin_game()
