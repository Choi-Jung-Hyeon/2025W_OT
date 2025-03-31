print("2차원의 공간의 좌표 <x,y>를 입력하세요:")
x=eval(input())
y=eval(input())
if(x>0 and y>0):
    print("<{0},{1}>는 1사분면에 속합니다.".format(x,y))
else:
    print("<{0},{1}>는 1사분면에 속하지 않습니다.".format(x,y))
if(x<0 and y>0):
    print("<{0},{1}>는 2사분면에 속합니다.".format(x,y))
else:
    print("<{0},{1}>는 2사분면에 속하지 않습니다.".format(x,y))
if(x<0 and y<0):
    print("<{0},{1}>는 3사분면에 속합니다.".format(x,y))
else:
    print("<{0},{1}>는 3사분면에 속하지 않습니다.".format(x,y))
if(x>0 and y<0):
    print("<{0},{1}>는 4사분면에 속합니다.".format(x,y))
else:
    print("<{0},{1}>는 4사분면에 속하지 않습니다.".format(x,y))
