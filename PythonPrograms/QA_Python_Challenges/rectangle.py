def area(length, width):
    length = (length)
    width = (width)
    area = length * width
    return f"The area is {area}^2"

def rectangle(length, width):
    perimeter = (2*length) + (2*width)
    print(f"The perimiter of the rectangle is {perimeter}")
    print(area(length, width))

data = rectangle(int(input("Enter the length: ")), int(input("Enter the width: ")))