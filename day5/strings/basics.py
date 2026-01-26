# creating strings
name = "ankush"
text = "python"

# indexing
print(text[0])
print(text[3])
print(text[-1])

# slicing
print(text[0:3])     # pyt
print(text[1:4])     # yth
print(text[-4:-1])   # tho

# looping through string
for ch in text:
    print(ch)

# string methods
print(len(text))
print(text.lower())
print(text.upper())

# strip example
msg = "   hello   "
print(msg.strip())

# replace example (strings are immutable)
text = text.replace("python", "world")
print(text)
