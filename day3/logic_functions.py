def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def biggest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def is_vowel(ch):
    return ch.lower() in ('a', 'e', 'i', 'o', 'u')
    
year = int(input("Enter year: "))
print("Leap year:", is_leap_year(year))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Biggest number:", biggest_of_three(a, b, c))

ch = input("Enter a character: ")
print("Is vowel:", is_vowel(ch))
