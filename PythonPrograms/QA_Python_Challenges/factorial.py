def fact(num):
    list1 = [num]
    answer = 1
    for entry in range(1,num):
        num = num - 1
        list1.append(num)
    for number in list1:
        answer = answer * number
    print(answer)
    
data = fact(int(input("Enter a number: ")))
