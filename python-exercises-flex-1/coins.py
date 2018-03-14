numb = 0
print("You have {} coins.".format(numb))
while True:
    switch = input("Do you want another? ")
    if switch == "yes":
        numb += 1
        print("You have {} coins.".format(numb))
    elif switch == "no":
        print("Bye")
        break