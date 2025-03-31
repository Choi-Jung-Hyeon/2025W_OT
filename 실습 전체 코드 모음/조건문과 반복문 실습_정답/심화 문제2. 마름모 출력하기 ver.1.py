#추가 문제3
n=int(input('마름모의 길이를 입력하세요. '))
for i in range(2*n-1):
    if i<n:
        for j in range(n-i-1):
            print(" ",end='')
        for j in range(2*(i+1)-1):
            if(j%2==0):
                print('*',end='')
            else:
                print(' ',end='')
        for j in range(n-i-1):
            print(" ",end='')
        print('')
    else:
        for j in range(i-n+1):
            print(' ',end='')
        for j in range (4*n-2*i-3):
            if(j%2==0):
                print('*',end='')
            else:
                print(' ',end='')
        for j in range(i-n+1):
            print(' ',end='')
        print('')
