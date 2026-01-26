def even_numbers(numbers):
    evens=[]
    for i in numbers:
        if i%2==0:
            evens.append(i) 
    return evens

numbers=[1,2,3,4,5,6]
print(even_numbers(numbers))

