def near(str):
    char_count = len(str)
    for char in range(0, char_count+1):
        front = str[:char]
        back = str[char+1:]
        answer = front + back
        if answer == second_entry:
            print("True")
            exit()
    print("False")    

first_entry = input("Enter a word here: ")
second_entry = input("Enter a similar word here: ")
data = near(first_entry)