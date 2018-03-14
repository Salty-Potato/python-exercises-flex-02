secret_number = 5
quesh = "I am thinking of a number between 1 and 10. "
print(quesh)
while True:
   guess = int(input("What's the number? "))
   if guess == secret_number:
       print("Yes! You win!")
       break
   elif guess >= 6:
       print("{} is too high.".format(guess))

   elif guess <= 4:
        print("{} is too low.".format(guess))
   else:
       print("Nope, try again. ")