n = int(input("숫자를 입력하시오 :"))
tmp = 0
for i in range(n+1):
	tmp += 2**i
print("2^0부터 2^",n,"까지의 합은 ",tmp,"입니다")

