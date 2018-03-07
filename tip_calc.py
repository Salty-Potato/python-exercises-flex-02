total = input("Total bill amount? ")
total = float(total)

service = input("Level of service: (Good, Fair or Bad)? ")

split = input("Split how many ways? ")
split = int(split)

if service == "Good":
    tip = total * .20
elif service == "Fair":
    tip = total * .15
else:
    tip = total * .10
    
    
print("Tip: ${:.2f}".format(tip))
print("Bill + Tip: ${:.2f}".format(total + tip))
print("Amount per person: ${:.2f}".format((total + tip) / split))