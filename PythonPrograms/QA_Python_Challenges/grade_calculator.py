math_mark = int(input("Enter the Maths Mark: "))
chem_mark = int(input("Enter the Chemistry Mark: "))
phys_mark = int(input("Enter the Physics Mark: "))
mark = math_mark + chem_mark + phys_mark
percent = (mark / 300)*100

if percent >= 70:
    print("A")
elif percent >= 60 and percent < 70:
    print("B")
elif percent >= 50 and percent < 60:
    print("C")
elif percent >= 40 and percent < 50:
    print("D")
else:
    print("You failed")
