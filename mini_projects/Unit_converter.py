print("------------------------------------------------------------------------")
print("-------------------- Welcome to the unit concerter ---------------------")
print("Available options mentioned below:")
print("1. Weight")
print("2. Distance")
print("3. Currency")
print("4. Temperature")

def wt_change():
    while True:
        print("Available options in weights")
        print("1. Kilograms (kg)")
        print("2. Grams (g)")
        print("3. Pounds (lb)")
        print("4. Ounce (oz)")
        initial_unit = int(input("Enter the option: "))
        match initial_unit:
            case 1:
                print("Available options to change in weights")
                print("1. Grams (g)")
                print("2. Pounds (lb)")
                print("3. Ounce (oz)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = initial_val * 1000
                        print(f" {initial_val}kg = {final_val}g")
                    case 2:
                        final_val = initial_val * 2.205
                        print(f"{initial_val}kg = {final_val}lb")
                    case 3:
                        final_val = initial_val * 35.274
                        print(f"{initial_val}kg = {final_val}oz")
                    case _:
                        print("Invalid Type selected")
            case 2:
                print("Available options to change in weights")
                print("1. Kilograms (kg)")
                print("2. Pounds (lb)")
                print("3. Ounce (oz)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = initial_val / 1000
                        print(f" {initial_val}g = {final_val}kg")
                    case 2:
                        final_val = initial_val * 2.205 / 1000
                        print(f"{initial_val}g = {final_val}lb")
                    case 3:
                        final_val = initial_val * 35.274 / 1000
                        print(f"{initial_val}g = {final_val}oz")
                    case _:
                        print("Invalid Type selected")
            case 3:
                print("Available options to change in weights")
                print("1. Kilograms (kg)")
                print("2. Grams (g)")
                print("3. Ounce (oz)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = initial_val / 2.205
                        print(f" {initial_val}lb = {final_val}kg")
                    case 2:
                        final_val = initial_val * 1000 / 2.205
                        print(f"{initial_val}lb = {final_val}g")
                    case 3:
                        final_val = initial_val * 16
                        print(f"{initial_val}lb = {final_val}oz")
                    case _:
                        print("Invalid Type selected")
            case 4:
                print("Available options to change in weights")
                print("1. Kilorams (kg)")
                print("2. Grams (g)")
                print("3. Pounds (lb)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = initial_val / (2.205*16)
                        print(f" {initial_val}oz = {final_val}kg")
                    case 2:
                        final_val = initial_val * 1000 / (2.205*16)
                        print(f"{initial_val}oz = {final_val}g")
                    case 3:
                        final_val = initial_val / 16
                        print(f"{initial_val}oz = {final_val}lb")
                    case _:
                        print("Invalid Type selected")
            case _:
                print("Invalid Type selected")

        choice = input("Do you wish to continue in this mode (y/n): ")
        if choice.lower() == 'y':
             continue
        elif choice.lower() == 'n':
            break
        else:
             print("Invalid Choice!!")

def dist_change():
    while True:
        print("Available options in distances")
        print("1. Kilometre (km)")
        print("2. Metre (m)")
        print("3. Mile (Mi)")
        print("4. Yards (yd)")
        initial_unit = int(input("Enter the option: "))
        match initial_unit:
            case 1:
                print("Available options to change in distances")
                print("1. Metre (m)")
                print("2. Mile (Mi)")
                print("3. Yards (yd)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = initial_val * 1000
                        print(f" {initial_val}km = {final_val}m")
                    case 2:
                        final_val = initial_val * 0.621371
                        print(f"{initial_val}km = {final_val}Mi")
                    case 3:
                        final_val = initial_val * 1093.61
                        print(f"{initial_val}km = {final_val}yd")
                    case _:
                        print("Invalid Type selected")
            case 2:
                print("Available options to change in distances")
                print("1. Kilometre (km)")
                print("2. Mile (Mi)")
                print("3. Yards (yd)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = initial_val / 1000
                        print(f" {initial_val}m = {final_val}km")
                    case 2:
                        final_val = initial_val * 0.000621371
                        print(f"{initial_val}m = {final_val}Mi")
                    case 3:
                        final_val = initial_val * 1.09361
                        print(f"{initial_val}m = {final_val}yd")
                    case _:
                        print("Invalid Type selected")
            case 3:
                print("Available options to change in distances")
                print("1. Kilometre (km)")
                print("2. Metre (m)")
                print("3. Yards (yd)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = initial_val / 0.621371
                        print(f" {initial_val}Mi = {final_val}km")
                    case 2:
                        final_val = initial_val * 1000 / 0.621371
                        print(f"{initial_val}Mi = {final_val}m")
                    case 3:
                        final_val = initial_val * 1760
                        print(f"{initial_val}Mi = {final_val}yd")
                    case _:
                        print("Invalid Type selected")
            case 4:
                print("Available options to change in distances")
                print("1. Kilometre (km)")
                print("2. Metre (m)")
                print("3. Mile (Mi)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = initial_val * 0.0009144
                        print(f" {initial_val}yd = {final_val}km")
                    case 2:
                        final_val = initial_val * 0.9144
                        print(f"{initial_val}yd = {final_val}m")
                    case 3:
                        final_val = initial_val / 1760
                        print(f"{initial_val}yd = {final_val}Mi")
                    case _:
                        print("Invalid Type selected")
            case _:
                print("Invalid Type selected")

        choice = input("Do you wish to continue in this mode (y/n): ")
        if choice.lower() == 'y':
             continue
        elif choice.lower() == 'n':
            break
        else:
             print("Invalid Choice!!")

def cur_change():
    print("Currency mode is currently unavailable!!")

def temp_change():
    while True:
        print("Available options in temperature")
        print("1. Celsius (°C)")
        print("2. Fahrenheit (°F)")
        print("3. Kelvin (K)")
        initial_unit = int(input("Enter the option: "))
        match initial_unit:
            case 1:
                print("Available options to change in temperature")
                print("1. Fahrenheit (°F)")
                print("2. Kelvin (K)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = (initial_val * 9/5) + 32
                        print(f" {initial_val}°C = {final_val}°F")
                    case 2:
                        final_val = initial_val + 273.15
                        print(f"{initial_val}°C = {final_val}K")
                    case _:
                        print("Invalid Type selected")
            case 2:
                print("Available options to change in temperature")
                print("1. Celsius (°C)")
                print("2. Kelvin (K)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = (initial_val - 32) * 5/9
                        print(f" {initial_val}°F = {final_val}°C")
                    case 2:
                        final_val = ((initial_val - 32) * 5/9) + 273.15
                        print(f"{initial_val}°F = {final_val}K")
                    case _:
                        print("Invalid Type selected")
            case 3:
                print("Available options to change in temperature")
                print("1. Celsius (°C)")
                print("2. Fahrenheit (°F)")
                final_unit = int(input("Enter the option: "))
                initial_val = int(input("Enter the value: "))
                match final_unit:
                    case 1:
                        final_val = initial_val - 273.15
                        print(f" {initial_val}K = {final_val}°C")
                    case 2:
                        final_val = ((initial_val - 273.15) * 9/5) + 32
                        print(f"{initial_val}K = {final_val}°F")
                    case _:
                        print("Invalid Type selected")

"""
while True:
    while True:
        change_quantity = int(input("Enter the quantity you wish to change: "))
        if change_quantity == 1:
            print("Entering weight mode")
            wt_change()
            break
        elif change_quantity == 2:
            print("Entering distance mode")
            dist_change()
            break
        elif change_quantity == 3:
            print("Entering currency mode")
            cur_change()
            break
        elif change_quantity == 4:
            print("Entering temperature mode")
            temp_change()
            break
        else:
            print("Enter valid values!!")
    cont = input("Do you wish to continue (y/n): ")
    if cont.lower() == 'y':
        continue
    elif cont.lower() == 'n':
        break
    else:
        print("Invalid Value, Try again!!")
"""
