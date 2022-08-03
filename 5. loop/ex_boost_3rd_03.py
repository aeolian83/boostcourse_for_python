# Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.
# (단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)
# 중앙값: 정중앙에 있는 값
# 특정 두 숫자 사이의 수들을 리스트로 만드는 법

def find_even_number(n, m):
    list_1 = list(range(n, m+1))
    print(list_1)
    for i in list_1:
        if i % 2 != 0 :
            continue
        print(i, "짝수")
        if i == list_1[len(list_1) // 2]:
            print(i, "중앙값")
    return

def int_input():
    while True:
        a = input("첫 번째 수 입력: ")
        try:
            first_num = int(a)
            break
        except:
            print("잘못입력했습니다. 정수만 입력 가능합니다. ")
            continue
    while True:
        b = input("두 번째 수 입력: ")
        try:
            second_num = int(b)
            break
        except:
            print("잘못입력했습니다. 정수만 입력 가능합니다. ")
            continue
    print(first_num, second_num)
    return first_num, second_num
    
n, m = int_input()

find_even_number(n, m)
