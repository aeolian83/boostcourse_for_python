# Q4. 오늘 애인이 생겼다고 해봅시다. 100일을 기념하고 싶은데요.
# 날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수를 만들어 보겠습니다.
# 😲조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
# 😲조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.

month_01 = [i for i in range(1, 32)]
month_02 = [i for i in range(1, 31)]
month_03 = [i for i in range(1, 29)]
print(month_02)

year = [month_01, month_02, month_03]

print(year)
# for i in year[0]:
#     print(i)