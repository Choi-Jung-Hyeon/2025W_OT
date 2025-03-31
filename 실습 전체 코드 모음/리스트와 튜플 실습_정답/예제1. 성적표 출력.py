names = ["철수", "영희", "지용"]
scores = []

for i in range(3):
    s = []
    print("=========================")
    print(names[i], "성적 입력")
    s.append(int(input("국어 점수: ")))
    s.append(int(input("영어 점수: ")))
    s.append(int(input("수학 점수: ")))
    s.append(s[0]+s[1]+s[2])
    s.append(s[3]/3)
    scores.append(s)

print("=========================")
for i in range(3):
    print(names[i], scores[i][0], scores[i][1], scores[i][2], "총점: ", scores[i][3], "평균: ", scores[i][4])