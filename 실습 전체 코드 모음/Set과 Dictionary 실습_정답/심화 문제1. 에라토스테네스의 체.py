SIZE = 100000
isPrime = []
primeCount = 0

# isPrime 리스트 초기화
# isPrime[n]은 n이 prime인지 여부 저장, 이를 위해 SIZE보다 한 개 더 넣어줌
for i in range(SIZE+1) :
    isPrime.append(True)
isPrime[0] = isPrime[1] = False     # 0과 1은 소수가 아님

for num in range(2, SIZE+1) :       # 2부터 10만까지 순회
    if isPrime[num] :               # 소수일 때만
        primeCount += 1

        multiple = 2                # 소수의 배수들을 제외하기
        while True :
            if num * multiple > SIZE :
                break
            else :
                isPrime[num*multiple] = False   # 소수의 배수는 소수가 아님
                multiple += 1


print("1부터 {0}까지 소수의 수는 {1}개 입니다.".format(SIZE, primeCount))
