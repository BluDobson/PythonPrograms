number_list = []

for number in range (2000, 3201):
    number = int(number)
    if number % 7 == 0 and not number % 5 == 0 :
        number_list.append(number)

print(number_list)