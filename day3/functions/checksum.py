def square(n):
    return n*n

def even_odd(a):
  return a % 2 == 0

def greet(name):
    return "hello " + name

# main code starts here

n=int(input("enter the number:" ))
result1=square(n)
print(result1)

a=int(input("enter the number to check:" ))
result2 = even_odd(a)
print(result2)

name=input("enter the name:" )
result3 = greet(name)
print(result3)
