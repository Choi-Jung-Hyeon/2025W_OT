# Q4 - 끝말 잇기 놀이

words = []
last = 0
flag = True

print("끝말잇기 게임을 시작합니다")

one = input("첫 단어를 말해주세요:")
last = one[-1]
words.append(one)
print(one, "\n")
        
while True :
    one = input("다음 단어를 말해주세요:")
    
    if one in words :
        print("이미 사용한 단어입니다!")
        flag = False
    if one[0] != last :
        print("끝말이 일치하지 않습니다!")
        flag = False

    if not flag :
        break

    for word in words :
        print(word, end="->")
    print(one, "\n")
    words.append(one)
    
    last = one[-1]
