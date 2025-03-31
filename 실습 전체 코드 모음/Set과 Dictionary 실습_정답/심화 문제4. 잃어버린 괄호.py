num = 0
hap = 0
sub = False
Equation = input("식을 입력하세요: ")

for char in Equation:
    if char != '+' and char != '-':
        num = 10 * num + (int(char))
    else:
        if not sub:
            hap += num
        else:
            hap -= num
        num = 0
        if char == '-':
            sub = True

#마지막 숫자 계산
if not sub:
    hap += num
else:
    hap -= num

print("최솟값은", hap, "입니다.")
