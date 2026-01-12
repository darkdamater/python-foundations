print('''if you want to convert Celcius to farhenhiet then press 1
          if you want to convert fehenheit to celcius then press 2''' )

a=input("enter")

if a == "1":
    temp= float(input("enter temperature in celcius:"))
    farhenhiet = (temp*1.8)+32
    print("temperature is farhenhiet",farhenhiet)
else:
    temp= float(input("enter temperature in farhenhiet:"))
    celcius = (temp-32)*5/9
    print("temperature is celcius",celcius)