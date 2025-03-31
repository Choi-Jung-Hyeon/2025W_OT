import random

def generate_numbers():
    nine=[[random.randrange(0,10),random.randrange(0,10),random.randrange(0,10)], \
          [random.randrange(0,10),random.randrange(0,10),random.randrange(0,10)], \
          [random.randrange(0,10),random.randrange(0,10),random.randrange(0,10)]]
    return nine

def check_numbers(a,b,c):
    score=0
    if(a==b):
        score=score+1
    if(a==c):
        score=score+1
    if(b==c):
        score=score+1
    if(score==3):
        score=score-1
        if(a==7):
            score=5
    return score

def check_nine_numbers(nine):
    total=0
    score=check_numbers(nine[0][0],nine[0][1],nine[0][2]) #첫 번째 가로 라인
    print("첫 번째 가로 라인에서 {0}점".format(score))
    total=total+score
    score=check_numbers(nine[1][0],nine[1][1],nine[1][2]) #두 번째 가로 라인
    print("두 번째 가로 라인에서 {0}점".format(score))
    total=total+score
    score=check_numbers(nine[2][0],nine[2][1],nine[2][2]) #세 번째 가로 라인
    print("세 번째 가로 라인에서 {0}점".format(score))
    total=total+score
    print("")
    
    score=check_numbers(nine[0][0],nine[1][0],nine[2][0]) #첫 번째 세로 라인
    print("첫 번째 세로 라인에서 {0}점".format(score))
    total=total+score
    score=check_numbers(nine[0][1],nine[1][1],nine[2][1]) #두 번째 세로 라인
    print("두 번째 세로 라인에서 {0}점".format(score))
    total=total+score
    score=check_numbers(nine[0][2],nine[1][2],nine[2][2]) #세 번째 세로 라인
    print("세 번째 세로 라인에서 {0}점".format(score))
    total=total+score
    print("")
    
    score=check_numbers(nine[0][0],nine[1][1],nine[2][2]) #첫 번째 대각선
    print("첫 번째 대각선에서 {0}점".format(score))
    total=total+score
    score=check_numbers(nine[0][2],nine[1][1],nine[2][0]) #두 번째 대각선
    print("두 번째 대각선에서 {0}점".format(score))
    total=total+score
    print("")

    print("총 점수는 {0}점".format(total))

arr=generate_numbers()
for i in range(3):
    for j in range(3):
        print(str(arr[i][j])+" ",end='')
    print("")
print("")
check_nine_numbers(arr)
