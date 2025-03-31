# Q3 - 핸드폰 가게

phones = {}

for i in range(0, 4) :
    name = input("휴대폰 이름: ")
    sell = int(input("판매 실적: "))
    grade = int(input("고객 평가: "))

    phones[name]= [sell, grade]

for a in phones.keys() :
    if phones[a][0] >= 4 and phones[a][1] >= 4 :
        print("우수 제품:", a, "판매실적:", phones[a][0], "고객평가:", phones[a][1])

