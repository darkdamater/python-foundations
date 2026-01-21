# creating lists
names = ["ankush", "akash", "aman"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "ankush", 3.4]

# printing lists
print(names)
print(numbers)
print(mixed)

# indexing in lists
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[-1])

# modifying list element
numbers[1] = 99
print(numbers)

# adding element to list
numbers.append(33)
print(numbers)

# length of a list
print(len(numbers))

# looping through list
for name in names:
    print(name)
