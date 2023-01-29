t=n = int(input("enter a number:"))
s = 0
while n>0:
    d = n % 10
    f = 1
    for i in range(2,d+1):
        f*=i
    s += f
    n //= 10
if t == s:
    print('strong')
else:
    print('not strong')