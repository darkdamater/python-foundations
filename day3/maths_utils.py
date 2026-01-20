def sum_n_numbers(n):
    total=0
    for i in range(1,n+1):
     total=total+i
    return total

def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(n * i)
    return table


def rev_number(number):
    rev_num=0
    while number>0:
     last_digit=number%10
     rev_num=rev_num*10+last_digit
     number=number//10
    return rev_num 


n = int(input("Enter a number: "))

print("Sum of first", n, "natural numbers:", sum_n_numbers(n))
print("Multiplication table:", multiplication_table(n))
print("Reversed number:", rev_number(n))
