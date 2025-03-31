# 유클리드 호제법 이용
def gcd (x, y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

print(gcd(8,12))
print(gcd(18,12))
