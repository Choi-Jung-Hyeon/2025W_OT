print("첫 번째 2차원 공간의 두 점 <x1, y1>,<x2, y2>를 입력하세요: ")


x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
print("두 번째 2차원 공간의 두 점 <x3, y3>,<x4, y4>를 입력하세요: ")

x3=eval(input())
y3=eval(input())
x4=eval(input())
y4=eval(input())
print("<x1,y1>,<x2,y2>의 값은 <{0},{1}>,<{2},{3}>".format(x1,y1,x2,y2))
print("<x3,y3>,<x4,y4>의 값은 <{0},{1}>,<{2},{3}>".format(x3,y3,x4,y4))
if((y2-y1)/(x2-x1)==(y4-y3)/(x4-x3)):
    print("두 직선은 평행합니다.")
else:
    print("두 직선은 평행하지 않습니다.")
    
