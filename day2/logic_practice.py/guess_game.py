secrete_word="python"
guess=""


while guess!= secrete_word:
    guess=input("enter your guess: ")
    if guess== secrete_word:
        print("you win!")
    else:
        print("try again!")
        