def vov_check(ch):
    if ch in('a','e','i','o','u','A','E','I','O','U'):
        print("vowel")
    else:
        print("consonant")    
ch=input("enter the character: ")
vov_check(ch)