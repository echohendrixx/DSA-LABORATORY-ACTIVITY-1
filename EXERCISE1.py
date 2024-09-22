# Makes the user to input the value of the temperature that they would like to convert
temp = float(input("Please input the temperature you want to convert: "))

# Makes the user input the conversion type of the temperature
unit = input("Please input the type of conversion you want to perform. Type CF in you want to convert Celsius to Farenheit or FC if you want to convert Farenheit to Celsius").upper()


# Performs the selected conversion type based on what the user selected
if unit == "CF":
    print(f"{temp}°C is equal to {temp * 9/5 + 32}")
elif unit == "FC":
    print(f"{temp}°F is equal to {(5/9 * (temp - 32))}")
else:
    print("Invalid input. Please try again.")
