while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    if choice < 1 or choice > 5:
        print("Invalid choice")
        continue

    num_1=float(input("enter the 1st number"))
    num_2=float(input("enter the 2nd number"))

    if choice  == 1:
        result= num_1 + num_2
        print(result)
    elif choice  == 2:
        result= num_1 - num_2
        print(result)
    elif choice  == 3:
        result= num_1 * num_2
        print(result)
    else :
        if num_2 ==0:
         print("error")
        else:
         result= num_1 / num_2
         print(result)
  