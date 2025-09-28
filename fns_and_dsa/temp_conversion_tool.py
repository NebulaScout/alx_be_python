FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp = float(input("Enter the temperature value: "))
    scale = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if scale == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted:.2f}°F")
    elif scale == 'F':
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted:.2f}°C")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()