def play():
    import random
    secret_number = random.randint(1, 10)
    quesh = "I am thinking of a number between 1 and 10. "
    count = 4
    
    print(quesh)
    print("You have 5 guesses left ")
        
    while True:
        guess = int(input("What's the number? "))
        if guess == secret_number:
            print("Yes! You win!")
            count = 4
            break
        elif count <= 0:
            print("You're out of guesses! Game over.")
            break
        elif guess >= secret_number and count >=1:
            count -=1
            print("{} is too high.".format(guess))
            print("You have {} guesses left ".format(count))
               
        elif guess <= secret_number  and count >=1:
            print("{} is too low.".format(guess))
            print("You have {} guesses left ".format(count))
            count -=1
        else:
            print("Nope, try again")
           
    while True:
        answer = input("Do you want to play again (Y or N)? ").upper()
        if answer == 'Y':
            play()
        elif answer == 'N':
            break
        else:
            print("I dont understand")
           
           
play()