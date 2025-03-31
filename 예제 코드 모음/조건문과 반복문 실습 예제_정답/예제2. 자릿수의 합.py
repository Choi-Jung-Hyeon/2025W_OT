# (0 < N <= 1,000,000) 조건 무시

N = int(input("숫자를 입력하시오: :"))

'''
while(True):
    try:
        N = int(input("숫자를 입력하시오: :"))
        break
    except:
        print("error 숫자가 아닙니다, 다시 입력하세요.")   
'''

saved_N = N
result = 0

while(N != 0):
    result = result + (N % 10)
    N = int(N / 10)

print (str(saved_N)+"의 자릿수의 합은 "+str(result)+" 입니다.")

'''
Test Case
12910291029의 자릿수의 합은 36 입니다.
99102의 자릿수의 합은 21 입니다.
0의 자릿수의 합은 0 입니다.
'''
