# Q1. 컴퓨터와 함께하는 가위바위보 게임을 만들어봅시다!
# 조건1 : 함수의 인자로는 나의 가위바위보 선택이 들어감
# 조건2 : 누가 무엇을 냈고, 누가 승리 했는지 출력이 되어야 함

import random

def game_input():
    player = input("가위 바위 보를 입력하시오(0, 1, 2를 입력할 수 있음) : ")
    try:
        player_code = int(player)
        if player_code > 2:
            player = 3
        elif player_code == 0:
            player = "가위"
        elif player_code == 1:
            player = "바위"
        elif player_code == 2:
            player = "보"
    except:
        rcp = ["가위", "바위", "보"]
        if player not in rcp :
            player = 4
    return player

def game_eval():
    win = "당신이 이겼습니다!"
    lose = "당신은 졌습니다."
    player = game_input()
    computer_code = random.randint(0, 2)
    if computer_code ==  0:
        computer = "가위"
    elif computer_code == 1:
        computer = "바위"
    elif computer_code == 2:
        computer = "보"
    if player == 3:
        print("0에서 2사이의 정수만 입력 할 수 있습니다.")
        return
    if player == 4:
        print("가위, 바위, 보 아니면 0, 1, 2 만 입력 할 수 있습니다.")
        return
    else:
        print("컴퓨터는", computer, "당신은", player, "를 선택했습니다.")
        if player == computer:
            print("비겼습니다.")
        elif player == "가위":
            if computer == "바위":
                print(lose)
            elif computer == "보":
                print(win)
        elif player == "바위":
            if computer == "가위":
                print(win)
            elif computer == "보":
                print(lose)
        elif player == "보":
            if computer == "가위":
                print(lose)
            elif computer == "바위":
                print(win)
        return

def game_start():
    while True:
        game_eval()
        while True:
            game_continue = input("게임을 계속하시겠습니까?(Y/N로 입력하시오): ")
            if game_continue in ("n", "N"):
                print("게임을 종료합니다.")
                return
            elif game_continue in ("Y", "y"):
                break
            else:
                print("잘못입력했습니다. 다시 입력하세요.")
                continue

game_start()