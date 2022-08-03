# Q2. 가위바위보 업그레이드 버젼을 함수로 만들어 봅시다. 아래와 같은 조건을 만족해 주세요.
# 조건 1: 게임을 몇 판을 진행할 것인지 입력을 받아주기
# 조건 2: 0, 1, 2, "가위", "바위", "보" 이외에 다른 입력을 받으면 재입력 받기
# 조건 3: 게임종료 후 나와 컴퓨터의 총 전적 출력하기

import random

def game_input():
    com_num = random.randint(0, 2)
    while True:
        player_input = input("가위(0) 바위(1) 보(2)를 입력하세요.(숫자로도 입력가능): ")
        dic = {"가위":0, "바위":1, "보":2}
        error = "입력은 가위 바위 보 또는 0 1 2로만 가능합니다."
        try:
            player_num = int(player_input)
            if player_num > 2:
                print(error)
                continue
            break
        except:
            if player_input in dic:
                player_num = dic[player_input]
                break
            else:
                print(error)
                continue
    return player_num, com_num

def game_core(player_num, com_num):
    result_eval = ["무승부!", "Player승!", "Com승!"]
    result = player_num - com_num
    return result_eval[result]

def game_start():
    while True:
        game = input("몇판 진행하시겠습니까?: ")
        error = "정수로만 입력 가능합니다."
        try:
            game_count = int(game)
            if game_count - float(game) != 0.0:
                print(error)
                continue
            break
        except:
            print(error)
            continue
    game_dic = {0:"가위", 1:"바위", 2:"보"}
    game_result_list = []
    for i in range(1, game_count + 1):
        player_num, com_num = game_input()
        game_result = game_core(player_num, com_num)
        print(f"Player: {game_dic[player_num]}")
        print(f"Com: {game_dic[com_num]}")
        print(f"{i}번째판 {game_result}")
        game_result_list.append(game_result)

    player_win = game_result_list.count("Player승!")
    com_win = game_result_list.count("Com승!")
    draw = game_result_list.count("무승부!")
    print()
    print(f"Player전적: {player_win}승, {draw}무, {com_win}패")
    print(f"Com전적: {com_win}승, {draw}무, {player_win}패")
    return

game_start()