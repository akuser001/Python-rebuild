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
wt_change()
