isbn = input("Please enter the ISBN as a 12 digit number: ")

d1 = int(isbn[0])
d2 = int(isbn[1])*3
d3 = int(isbn[2])
d4 = int(isbn[3])*3
d5 = int(isbn[4])
d6 = int(isbn[5])*3
d7 = int(isbn[6])
d8 = int(isbn[7])*3
d9 = int(isbn[8])
d10 = int(isbn[9])*3
d11 = int(isbn[10])
d12 = int(isbn[11])*3

check_number = 10 - ((d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12)%10)

print(f"For the isbn {isbn}, the check number is {check_number}")