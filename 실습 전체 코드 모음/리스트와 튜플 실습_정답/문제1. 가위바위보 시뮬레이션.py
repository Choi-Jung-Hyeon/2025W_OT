# Q1 - 가위바위보 시뮬레이션

weapon = [ "바위", "보", "가위"]
wins = [[0, 2], [1, 0], [2, 1]]

first = int(input("첫 번째 사람을 입력하시오: "))
second = int(input("두 번째 사람을 입력하시오: "))

print("첫 번째 사람:", weapon[first])
print("두 번째 사람:", weapon[second])

if [first, second] in wins:
    print("첫 번째 사람이 이겼습니다.")
elif [second, first] in wins:
    print("두 번째 사람이 이겼습니다.")
else:
    print("비겼습니다.")
