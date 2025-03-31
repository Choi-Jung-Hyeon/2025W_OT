# 추가문제 - 워드 카운트 프로그램

wordList = []
wordCount = {}

line = input("문장 입력 :")

start = 0
for idx in range(len(line)) :
    if line[idx] == ' ' and start!=idx:
        wordList.append(line[start:idx])
        start = idx + 1
    elif line[idx]==' ' and start==idx:
        start=idx + 1
wordList.append(line[start:len(line)])

for word in wordList :
    wordCount[word] = 0
for word in wordList :
    wordCount[word] = wordCount[word] + 1

print("전체 단어:", len(wordList))
print("유니크 단어:", len(wordCount.keys()))

i=0
for key in wordCount.keys() :
    if wordCount[key] > 1 :
        if i>=1:
            print(", ",end='')
        else:
            print("중복 출현 단어:",end = '')
        print(key, wordCount[key],end='')
        i+=1
