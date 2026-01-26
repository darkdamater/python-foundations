text=input("enter the text").lower()

count =0

for ch in text:
    if ch in "aeiou":
        count+= 1

print("the number of wovels:",count)



