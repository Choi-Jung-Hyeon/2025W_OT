#Q2 백화점 할인율 계산하기
DressNum = int(input("원피스의 개수를 입력하시오: "))
SweaterNum = int(input("스웨터의 개수를 입력하시오: "))

Total = DressNum * 50000 + SweaterNum * 30000

if Total >= 200000:
    print("총액: ", int(Total*0.8))
elif Total < 100000:
    print("총액: ", int(Total*0.95))
else:
    print("총액: ", int(Total*0.9))
