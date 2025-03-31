n=int(input("Input the number: "))
original=n
reverse=0
while n>0:
    reverse *= 10
    reverse += n%10
    n = n//10
print("The sum of two numbers is: {0}.".format(original+reverse))
    
