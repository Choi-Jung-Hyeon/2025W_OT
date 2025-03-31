N = set([1,2,3,4,5])
n = input("n: ")
set_n = set()
for i in range(len(n)):
    set_n.add(int(n[i]))

if N == set_n:
    print("n(%s)은 12345와 쌍둥이 입니다." % n)
else:
    print("n(%s)은 12345와 쌍둥이가 아니며, 포함되지 않는 숫자들은" % n, set_n.difference(N), "입니다.")