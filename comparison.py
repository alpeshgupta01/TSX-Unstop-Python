x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
def compare(x, y):
    if x > y:
        return f"{x} is greater than {y}"
    elif x < y:
        return f"{x} is less than {y}"
    else:
        return f"{x} is equal to {y}"
print(compare(x, y))