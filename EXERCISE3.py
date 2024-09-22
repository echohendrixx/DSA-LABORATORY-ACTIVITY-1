# Prompt the user to input an odd integer for the width of the diamond
width = int(input("Please input an odd number to specify the width of the diamond you want to create: "))

# Checks if the user entered an odd or even integer. If it is an odd, it then starts to create a diamond with the width depending on the value they had entered.
if width % 2 == 1:
    for i in range (width//2 + 1):
        print(" " * (width//2 - i) + "*" * (2 * i + 1))
    for i in range(width//2 -1, -1, -1):
        print(" " * (width//2 - i) + "*" * (2 * i + 1))
else:
    print("Please provide an odd integer!")
