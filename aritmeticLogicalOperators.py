x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):           
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y
def modulus(x, y):
    return x % y
def exponent(x, y):
    return x ** y
def floor_division(x, y):
    return x // y
def logical_and(x, y):
    return x and y
def logical_or(x, y):
    return x or y
def logical_not(x):
    return not x
def logical_xor(x, y):
    return (x and not y) or (not x and y)
def bitwise_and(x, y):
    return x & y
def bitwise_or(x, y):
    return x | y
def bitwise_not(x):
    return ~x
def bitwise_xor(x, y):
    return x ^ y
def bitwise_left_shift(x, y):
    return x << y
def bitwise_right_shift(x, y):
    return x >> y
def main():                 
    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))
    print("Modulus:", modulus(x, y))
    print("Exponent:", exponent(x, y))
    print("Floor Division:", floor_division(x, y))
    print("Logical AND:", logical_and(x, y))
    print("Logical OR:", logical_or(x, y))
    print("Logical NOT x:", logical_not(x))
    print("Logical NOT y:", logical_not(y))
    print("Logical XOR:", logical_xor(x, y))
    print("Bitwise AND:", bitwise_and(x, y))
    print("Bitwise OR:", bitwise_or(x, y))
    print("Bitwise NOT x:", bitwise_not(x))
    print("Bitwise XOR:", bitwise_xor(x, y))
    print("Bitwise Left Shift x by 2:", bitwise_left_shift(x, 2))
    print("Bitwise Right Shift x by 2:", bitwise_right_shift(x, 2))
if __name__ == "__main__":
    main()