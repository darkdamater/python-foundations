text=input("enter the text: ").upper()
char_freq={}

for ch in text:

    if ch ==" ":
        continue

    if ch in char_freq:
        char_freq[ch]+=1

    else:
        char_freq[ch]= 1

print(char_freq)

max_count=0
max_char=""

for ch, count in char_freq.items():
    if count>max_count:
        max_count=count
        max_char=ch

print("Most frequent character:", max_char)
print("Frequency:", max_count)

