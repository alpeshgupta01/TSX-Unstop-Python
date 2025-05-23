a = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the width of the rectangle: "))
def area(a, b):
    return a * b
def perimeter(a, b):
    return 2 * (a + b)

print("Area of the rectangle:", area(a, b))
print("Perimeter of the rectangle:", perimeter(a, b))