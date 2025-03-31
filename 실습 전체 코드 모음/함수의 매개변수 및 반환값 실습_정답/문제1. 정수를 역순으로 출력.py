def print_reverse(num):
    if num>0:
        print(num%10,end="")
        print_reverse(num//10)
        
print_reverse(124)
print("")
print_reverse(11234)
