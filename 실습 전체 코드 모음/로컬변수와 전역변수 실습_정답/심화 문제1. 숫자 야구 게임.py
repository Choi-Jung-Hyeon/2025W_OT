import random
ans = []
def baseball ():
    for i in range(1,10):
        strike=0
        ball=0
        user=[0, 0, 0]
        print("*** BASEBALL GAME .... ROUND :",i)
        user[0] = int(input("1st number: "))
        user[1] = int(input("2nd number: "))
        user[2] = int(input("3rf number: "))
           
        for j in range(0,3):
            for k in range(0,3):
                if ans[j]==user[k]:
                    if j==k:
                        strike+=1
                    else:
                        ball+=1
        print("COMPUTER :",end="")
        if strike==0:
            if ball==0:
                print(" O U T   !!!!")
            else:
                print(ball,"BALL !!!!")
        else:
            if ball==0:
                print(strike,"STRIKE !!!!")
            else:
                print(strike,"STRIKE,",ball,"BALL !!!!")
        if strike==3:
            print("USER WINNER !!!!")
            return 
        
    print("COMPUTER WINNER !!!!")
    print(" The numbers are",ans[0],ans[1],str(ans[2])+".")
    
while True:
    play = input("Play game? (y,n) : ")
    ans = []
    for i in range(0,3):
        n = random.randrange(1,10)
        while n in ans:
            random.randrange(1,10)
        ans.append(n)
    print(ans)
    if play=="y":
        baseball()
    else:
        break
