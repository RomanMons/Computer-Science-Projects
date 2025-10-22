w = int(input("Enter weight (g): "))
h = int(input("Enter height (cm): "))
d = int(input("Enter diameter (cm): "))
if w<=2000 and h<=90 and (h+d*2)<=104:
    print("Yes")
else:
    print("No")
