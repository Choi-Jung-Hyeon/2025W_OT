M=int(input(''))
F=M+1#총 몇개
flag=2
i=M-1#현재 몇개 찍어야하는지
#1:-> 2: 밑 3: <- 4: 위

N=(M-1)*M+1#현재 숫자 몇이 찍혀있는지
for j in range(M):
    print(1+j*M,end=' ')

while F<M*M:
    if flag==1:
        for j in range(i):
            N=N+M
            print(N,end=' ')
            F=F+1
        i=i-1
        flag=2
#    print('\n',flag)
    if flag==2:
        for j in range(i):
            N=N+1
            print(N,end=' ')
            F=F+1
        flag=3
    if flag==3:
        for j in range(i):
            N=N-M
            print(N,end=' ')
            F=F+1
        i=i-1
        flag=4
    if flag==4:
        for j in range(i):
            N=N-1
            print(N,end=' ')
        flag=1
