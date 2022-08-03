# Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.
# 소수: 1과 자기 자신만을 약수로 가지는 수

def prime_number_list(a, b):
    # 에라토스테네스의 체 알고리즘을 이용해서 a, b 두 수사이의 소수를 구해 리스트를 만들고
    # 그 리스트의 길이를 측정해서 숫자로 print합니다. 
    sieve = [True] * b

    m = int(b ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, b, i):
                sieve[j] = False
    prime_list_2 = [i for i in range(a, b) if sieve[i] == True]
    # print(prime_list_2)
    print(f"{a}와 {b}사이에 존재하는 소수의 개수는{len(prime_list_2)}개 입니다")
    return

def int_input():
    # input을 두번 받고, 숫자로만 입력 가능하도록 예외를 설정했고
    # 특히 두번째 수는 첫번째 수보다 커야 입력이 되도록 했습니다. 
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
            if first_num >= second_num:
                print("두번째 수는 첫번째 수보다 커야 합니다.")
                continue
            break
        except:
            print("잘못입력했습니다. 정수만 입력 가능합니다.")
            continue
    # print(first_num, second_num)
    return first_num, second_num

a, b = int_input()
prime_number_list(a, b)