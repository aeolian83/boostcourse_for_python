korea_age = int(input("한국나이를 입력하세요: "))
birth = input("생일이 지났습니까?(y/n): ")

if birth == 'y' or birth == 'Y' :
    print('당신의 미국나이는:', korea_age - 1, '입니다')
elif birth == 'n' or birth == 'N':
    print('당신의 미국나이는:', korea_age - 2, '입니다')
else:
    print('잘못 입력했습니다.')