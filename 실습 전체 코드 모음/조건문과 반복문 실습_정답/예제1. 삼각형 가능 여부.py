#Q1 삼각형 가능 여부
a = int(input())
b = int(input())
c = int(input())

if a > 0 and b > 0 and c > 0:
    if a+b > c and a+c > b and b+c > a:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
