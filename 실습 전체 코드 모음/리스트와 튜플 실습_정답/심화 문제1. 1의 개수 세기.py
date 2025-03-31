# 1부터 n까지 하나하나 세기
def countByBrute(n) :
    count = 0
    for now in range(1, n+1) : # 1부터 n까지 
        count += countOne(now)

    return count

# num에 1이 들어있는 갯수 세기
def countOne(num) :
    count = 0
    while num > 0 : # 자리수마다 반복하면서
        if num % 10 == 1 :
            count += 1
        num = num // 10
    return count

# 재귀문을 이용하여 조금 똑똑하게 세기, 100만이 넘을 땐 위 코드는 너무 느리다!
# 세 부분으로 나눈다.
# part1 : 그 전 자리수에 사용된 1의 갯수 (2325라면 1부터 999까지 사용된 1의 갯수)
# part2 : 그 자리수에서 사용된 맨 앞 1의 수(2325라면, 1000~1999까지 맨 앞 1의 갯수)
# part3 : 다음 자리수에서 사용된 1의 수(2325라면, 325동안 쓰인 1의 갯수)
PRECALC = []
for i in range(10) :
    PRECALC.append( i * 10**(i-1) )
    
def countBySmart(n) :
    # 재귀문의 기저 조건 : 0일땐 0, 1자리수면 무조건 1
    if n == 0 : return 0
    if n < 10 : return 1    
    
    size = 0        # 자릿수 계산
    firstNumber = 0 # 맨 앞 자리 수
    t = n
    while t > 0 :
        firstNumber = t % 10
        t = t // 10
        size += 1
    
    part1 = PRECALC[size-1] * firstNumber         # part1
    
    # part2
    if firstNumber != 1 :
        part2 = 10 ** (size-1)
    else :
        part2 = n % 10**(size-1) + 1
        
    part3 = countBySmart(n % 10**(size-1))       # part3

    return part1 + part2 + part3
    
########################################################
inputN = int(input())
print(countByBrute(inputN))
print(countBySmart(inputN))
