H = int(input("Height? "))
W = int(input("Width? "))

print("*" * H)
        
for i in range(1, W):
        print("*" + ((W-2) * " ") + "*")
        
print("*" * H)