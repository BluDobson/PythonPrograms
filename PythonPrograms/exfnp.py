def grade(number1, number2, number3):
    answer = ((number1 + number2 + number3) * 100) / 175
    return answer

def mark(mark_number):
    if mark_number >= 90:
        answer = "A*"
    elif mark_number >= 80 and mark_number < 90:
        answer = "A" 
    elif mark_number >= 70 and mark_number < 80:
        answer = "B"
    elif mark_number >= 60 and mark_number < 70:
        answer = "C" 
    else:
        answer = "Fail"
    return answer

name = input("Enter your name here: ")
percent = grade(int(input("Enter the homework score: ")), int(input("Enter the assessment score: ")), int(input("Enter the final exam score:")))
letter_mark = mark(percent)

print(f"{name}: {percent}%, you got a {letter_mark}")