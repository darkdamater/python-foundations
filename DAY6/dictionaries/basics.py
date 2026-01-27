#dictionaries are used in py to store key value pairs 
students={
    "name":"Ankush",
    "age":21,
    "branch":"cse",
}
#accessing the values
print(students["name"])
print(students["branch"])

#adding and updating a value
students["college"]="xyz"
students["age"]=33

print(students)

#looping in dictionary
for key in students:
    print(key)

for value in students.values():
    print(value)

#looping through key value pair

for key, value in students.items():
    print(key, value)

#check if the key exists
if "name" in students:
    print("Key exists")


