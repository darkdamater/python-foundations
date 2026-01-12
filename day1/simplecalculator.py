num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
choice=input("choose the operation(1,2,3,4):")

if choice == "1":
    result= num1+num2
    print("result is=",result)
elif choice == "2":
    result= num1-num2
    print("result:",result)
elif choice == "3":
    result= num1*num2
    print("result:",result)
elif choice == "4":
  if num2 !=0 :
    result= num1/num2
    print("result:",result)
  else:
    print("error")
else:
    print("no operator selected")