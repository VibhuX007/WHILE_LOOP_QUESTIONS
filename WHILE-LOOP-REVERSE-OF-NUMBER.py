#PRINT REVERSE OF A NUMBER USING WHILE LOOP?
a=123
b=0
while a!= 0:
    digit = a % 10
    b=a*10+digit
    a //= 10
print(str(a))


