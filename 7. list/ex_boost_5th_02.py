# Q2. 다음과 같이 학생들의 시험 답지가 있습니다. 그리고 답안지도 있습니다.
# - 함수를 하나 만들어 채점을 하고 학생들의 점수를 출력하고 등수도 함께 출력해주세요.

# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

# 함수 
def evaluate_rank(s, a):
    student_eval = [] # 함수에서 점수를 평가해서 [점수, 학생이름]형태로 리스트를 작성합니다. 
    for answer in s: # 학생 한명씩 평가합니다. 
        answer_seq = 0
        evaluation = [] # 점수를 작성하기 위해 정답과 오답을 불린 형태로 리스트를 만들게 됩니다. 
        name = answer[:2] # 이름을 출력하기 위해 슬라이싱을 이용합니다. 
        for i in answer[3:13]: # 정답부분을 슬라이싱을 통해 떼어내서 그안에서 for문으로 반복합니다.  
            if int(i) == a[answer_seq]: # 학생들이 제출한 답안은 str로 작성되어 있기 때문에 int로 변환해서 답안과 비교합니다. 
                evaluation.append(True) # 정답이면 True
            else:
                evaluation.append(False) # 오답이면 False를 evlauation리스트에 집어 넣습니다. 
            answer_seq += 1
        score = evaluation.count(True) * 10 # True값의 개수를 세서 10을 곱해 점수를 도출합니다. 
        student_eval.append([score, name]) # [점수, 이름]으로 리스트를 작성합니다. 
    student_eval.sort(reverse=True) # 점수를 역순으로 정렬합니다. 

    for score, name in student_eval:
        rank_score = student_eval.index([score, name]) + 1 # 인덱스 값에 1을 더해서 등수를 도출합니다. 
        print(f"학생: {name}, 점수: {score}, {rank_score}등")

evaluate_rank(s, a)
