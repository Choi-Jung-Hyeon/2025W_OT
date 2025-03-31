import random
rand_num = random.randrange(1,100)

def check_num(n):
    if n == rand_num:
        return 0
    elif n < rand_num:
        return 1
    elif n > rand_num:
        return 2

print("Game Start!")
while True:
    n = int(input("n: "))
    ret = check_num(n)
    if ret == 0:
        print("SUCCESS")
        break
    elif ret == 1:
        print("UP")
    else:
        print("DOWN")