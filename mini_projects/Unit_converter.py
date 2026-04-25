print("------------------------------------------------------------------------")
print("-------------------- Welcome to the unit concerter ---------------------")
print("Available options are mentioned below:")
print("1. Weight")
print("2. Distance")
print("3. Temperature")

conversion = {
1:{
            'kg': {'g': 1000, 'lb': 2.20462, 'oz': 35.274},
            'g': {'kg': 0.001, 'lb': 0.00220462, 'oz': 0.035274},
            'lb': {'kg': 0.453592, 'g': 453.592, 'oz': 16},
            'oz': {'kg': 0.0283495, 'g': 28.3495, 'lb': 0.0625}
        },
2:{
            'm': {'km': 0.001, 'mi': 0.000621371, 'ft': 3.28084},
            'km': {'m': 1000, 'mi': 0.621371, 'ft': 3280.84},
            'mi': {'m': 1609.34, 'km': 1.60934, 'ft': 5280},
            'ft': {'m': 0.3048, 'km': 0.0003048, 'mi': 0.000189394}
        },
3: {
            'c': {'f': lambda x: (x * 9/5) + 32, 'k': lambda x: x + 273.15},
            'f': {'c': lambda x: (x - 32) * 5/9, 'k': lambda x: (x - 32) * 5/9 + 273.15},
            'k': {'c': lambda x: x - 273.15, 'f': lambda x: (x - 273.15) * 9/5 + 32}
        }
}
while True:
    mode = int(input("Enter the mode you want: "))
    if mode in conversion:
        try:
            from_unit = input("Enter the unit you want to convert from: ").lower()
            to_unit = input("Enter the unit you want to convert to: ").lower()
            value = float(input("Enter the value you want to convert: "))
            if from_unit in conversion[mode] and to_unit in conversion[mode][from_unit]:
                if mode == 3:
                    result = conversion[mode][from_unit][to_unit](value)
                else:
                    result = value * conversion[mode][from_unit][to_unit]
                print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
            else:
                print("Invalid units for the selected mode.")
        except ValueError:
            print("Invalid input. Please enter a number")
    else:
        print("Invalid mode. Please select a valid mode.")
    continue_choice = input("Do you want to perform another conversion? (yes/no): ")
    if continue_choice.lower() == 'yes':
        print("Resetting the converter for another conversion...")
    elif continue_choice.lower() == 'no':
        print("Thank you for using the unit converter. Goodbye!")
        break
    else:
        print("Invalid choice. Exiting the converter.")
        break
