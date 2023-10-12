#Activity #2 Write a Python program that will use function called calculate_perimeter that takes the length and width of a rectangle
#The Perimeter of a rectangle can be calculated using the formula : perimeter = 2 * (length + width)

def calculate_perimeter (length, width):
    perimeter = 2 * (length + width)
    return perimeter

length = int(input("length of a rectangle"))
width = int(input("width of a rectangle"))

x = calculate_perimeter (length, width)

print("The perimeter of a rectangle is ", x)