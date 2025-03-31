import random

def generate_numbers():
    three_numbers=[random.randrange(0,10),random.randrange(0,10),random.randrange(0,10)]
    return three_numbers

def check_numbers(three_numbers):
    score=0
    if(three_numbers[0]==three_numbers[1]):
        score=score+1
    if(three_numbers[0]==three_numbers[2]):
        score=score+1
    if(three_numbers[1]==three_numbers[2]):
        score=score+1
    if(score==3):
        score=score-1
        if(three_numbers[0]==7):
            score=5
    return score

cont=1
total=0
jackpot=0
while(cont==1):
    arr=generate_numbers()
    print("뽑힌 숫자 {0} {1} {2}".format(arr[0],arr[1],arr[2]))
    score=check_numbers(arr)
    if(score==5):
        jackpot=jackpot+1
    total=total+score
    print("얻은 점수:  {0}".format(score))
    stop=input("그만하시겠습니까? ")
    if(stop=="y" or stop=="Y"):
        cont=0
    print("")
print("총 점수:  {0} , 잭 팟 횟수:  {1}".format(total,jackpot))
