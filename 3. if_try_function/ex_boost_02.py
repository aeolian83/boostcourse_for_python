# Q2. 월급을 입력하면 연봉을 계산해주는 계산기를 만들어 봅시다. 세전 연봉과 세후 연봉을 함께 출력하도록 해봅니다.

def monthly_payment_cal():
    while True:
        monthly_payment = input("연봉을 입력해주십시오(숫자로 만원단위로 입력해주십시오)")
        try:
            month_pay = float(monthly_payment)
            break
        except:
            print("만원단위 정수로만 입력해주십시오")
            continue
    return month_pay

def yearly_pay_cal():
    month_pay = monthly_payment_cal()
    before_tax_pay = month_pay * 12
    if before_tax_pay > 50000:
        yearly_pay = before_tax_pay - (before_tax_pay * 0.42)
    elif before_tax_pay > 30000:
        yearly_pay = before_tax_pay - (before_tax_pay * 0.40)
    elif before_tax_pay > 15000:
        yearly_pay = before_tax_pay - (before_tax_pay * 0.38)
    elif before_tax_pay > 8800:
        yearly_pay = before_tax_pay - (before_tax_pay * 0.35)
    elif before_tax_pay > 4600:
        yearly_pay = before_tax_pay - (before_tax_pay * 0.24)
    elif before_tax_pay > 1200:
        yearly_pay = before_tax_pay - (before_tax_pay * 0.15)
    else:
        yearly_pay = before_tax_pay - (before_tax_pay * 0.06)
    print("세전연봉:", round(before_tax_pay), "만원")
    print("세후연봉:", round(yearly_pay), "만원")
    

yearly_pay_cal()