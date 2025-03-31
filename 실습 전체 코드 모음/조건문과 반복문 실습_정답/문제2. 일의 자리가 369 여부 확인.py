#Q3 일의 자리가 369 여부 확인
Num = int(input())
Result = Num % 10
print("Result: ", Result)

if Result == 0:
    print("No")
else:
    if Result % 3 == 0:
        print("Yes")
    else:
        print("No")
