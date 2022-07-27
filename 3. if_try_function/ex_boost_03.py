# Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.
# 이름과 점수, 학점 모두 출력하도록 해봅니다.

def name_score_input():
    st_name = input("학생이름을 입력해주세요: ")
    while True:
        print("학생의 점수를 입력해주세요(1~100사이의 정수로 입력필요)")
        st_score = input("(소숫점 이하는 버립니다): ")
        try:
            score = int(st_score)
            if score > 100:
                print("점수는 1~100사이의 정수로만 입력 가능합니다.")
                continue
            elif 0 > score:
                print("점수는 1~100사이의 정수로만 입력 가능합니다.")
                continue
            else:
                break
        except:
            print("점수는 1~100사이의 정수로만 입력 가능합니다.")
            continue
            
    return st_name, score

def st_grader():
    st_name, score = name_score_input()
    if score > 94:
        grade = "A+"
    elif score > 89:
        grade = "A"
    elif score > 84:
        grade = "B+"
    elif score > 79:
        grade = "B"
    elif score > 74:
        grade = "C+"
    elif score > 69:
        grade = "C"
    elif score > 64:
        grade = "D+"
    elif score > 59:
        grade = "D"
    else:
        grade = "F"
    print("--------------------------")
    print("학생이름:", st_name)
    print("점수: ", str(score) + "점")
    print("학점:", grade)
    return

st_grader()