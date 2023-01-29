#DEFINE A FUNCTION TO PRINT THE FACTORIAL OF A NUMBER?
def fac(n):
    s=1
    while n>0:
        s=s*n
        n=n-1
    print(s)
n=int(input('ENTER- '))
fac(n)
