def grid(num):
    for number in range (1,num+1):
        print(number, end="\t")
    print("\n")
    for number1 in range (1,num+1):
        for number2 in range (1,num+1):
            print(number1*number2, end="\t")
        print ("\n")
data = grid(int(input("Enter a number: ")))