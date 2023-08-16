def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input temperature in Celsius
celsius_temperature = float(input("Enter temperature in Celsius degrees: "))

# Convert Celsius to Fahrenheit
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

# Print the result
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit")
