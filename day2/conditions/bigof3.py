def bo3(a,b,c):
    if a>=b and a>=c :
        print(a,"is the biggest")
    elif b>=a and b>=c :
       print(b,"is the biggest")
    else :
        print(c,"is the biggest")

a=int (input("input number1 "))
b=int (input("input number2 "))
c=int (input("input number3 "))
bo3(a,b,c)
