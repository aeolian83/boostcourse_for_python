def age_method_input():
    while True:
        age = input("나이를 입력하시오: ")
        try:
            pass_age = int(age)
            if pass_age > 100:
                print("나이는 100까지만 입력가능합니다.")
                continue
            elif pass_age < 0:
                print("나이는 양의 정수로만 입력가능합니다.")
                continue
        except:
            print("나이는 숫자로만 입력가능합니다.")
            continue
        break
    while True:
        method_list = ["카드", "현금"]
        method = input("지불방법을 선택하시오(카드/현금): ")
        if method in method_list:
            break
        else:
            print("'카드'와 '현금'으로만 입력 가능합니다.")
            continue
    return pass_age, method

def bus_charge_cal():
    age, method = age_method_input()
    if age < 8:
        charge = "무료"
    elif age > 74:
        charge = "무료"
    elif age < 14:
        charge = "450원"
    elif age < 20:
        if method == "카드":
            charge = "720원"
        elif method == "현금":
            charge = "1000원"
    elif age < 75:
        if method == "카드":
            charge = "1200원"
        elif method == "현금":
            charge = "1300원"
    print("---------------------")
    print("나이: " + str(age) + "세")
    print("지불유형: " + method)
    print("버스요금: " + charge)
    return

bus_charge_cal()