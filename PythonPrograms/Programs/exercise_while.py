first_name = str(input("Enter a name: "))
names = [first_name]
count = 1

while count < 5:
    names.append(str(input("Enter a name: ")))
    count +=1

for name in names:
    print(f"{name} is awesome!")

