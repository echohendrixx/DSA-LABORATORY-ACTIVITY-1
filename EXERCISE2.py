# Makes the user to input what they want to calculate
ohmslaw = input("What do you want to calculate? Enter 'V' to calculate for Voltage, 'I' for Current, and 'R' for Resistance").upper()


# Performs the calculation depending on what the user selected
try:
    if ohmslaw == "V":
        I = float(input("Please input the value of the Current."))
        R = float(input("Please input the value of the Resistance."))
        V = I * R
        print(f"The Voltage is equal to {V}")
    elif ohmslaw == "I":
        V = float(input("Please input the value of the Voltage."))
        R = float(input("Please input the value of the Resistance."))
        I = V / R
        print(f"The Current is equal to {I}")
    elif ohmslaw == "R":
        V = float(input("Please input the value of the Voltage."))
        I = float(input("Please input the value of the Current."))
        R = V / I
        print(f"The Resistance is equal to {R}")
    else:
        print("Invalid input. Please enter 'V', 'I', or 'R'")

# Handle division by zero error
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Handle invalid numeric input
except ValueError as e:
    print(f"Error: {e}")
