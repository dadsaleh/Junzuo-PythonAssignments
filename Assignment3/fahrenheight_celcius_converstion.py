# F = (F - 32) * 5/9
# C = (C * 9/5) + 32

ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_C = -273.15
end_flag = False

temperature_value = float(
    input("Enter the temperature value you want to convert: ")
)  # Take the input as float
temperature_type = input(
    "Enter the temperature type (F for fahrenheit, C for celcius): "
)  # Take the type as a string

# Validate input:
# Match the temperature type with the proper fromula, and insure the input is not over absolute for that type
# Store the truth value of the choosen type to use for printing and compare operations
if (is_fahrenheit := (temperature_type == "F")) and temperature_value > ABSOLUTE_ZERO_F:
    temperature_value = (temperature_value - 32) * 5 / 9
elif (is_celcius := (temperature_type == "C")) and temperature_value > ABSOLUTE_ZERO_C:
    temperature_value = (temperature_value * 9 / 5) + 32
else:
    # Check what the faliure was and print the error message
    # Print the invalid temperature type message if the user did not choose a valid option
    # Else, the temperature_value must be over the absolute zero, so print that message
    print(
        "Invalid Temperature Type. Please enter either: 'F' for fahrenheit, 'C' for celcius."
    ) if (not (is_fahrenheit or is_celcius)) else print(
        "Invalid Temperature. Please input a temperature value over absolute zero."
    )
    end_flag = True

# Final display of the result if the end_flag is false
if not end_flag:
    print(f"The temperature in celcius is: ", end="") if is_fahrenheit else print(
        f"The temperature in fahrenheit is: ", end=""
    )
    print(f"{temperature_value:,.2f}")
