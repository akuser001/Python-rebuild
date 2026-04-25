print("------------------------------------------------------------------------")
print("-------------------- Welcome to the unit concerter ---------------------")
print("Available options mentioned below:")
print("1. Weight")
print("2. Distance")
print("3. Temperature")

wt_conversion = {
            'kg': {'g': 1000, 'lb': 2.20462, 'oz': 35.274},
            'g': {'kg': 0.001, 'lb': 0.00220462, 'oz': 0.035274},
            'lb': {'kg': 0.453592, 'g': 453.592, 'oz': 16},
            'oz': {'kg': 0.0283495, 'g': 28.3495, 'lb': 0.0625}
        }

dist_conversion = {
            'm': {'km': 0.001, 'mi': 0.000621371, 'ft': 3.28084},
            'km': {'m': 1000, 'mi': 0.621371, 'ft': 3280.84},
            'mi': {'m': 1609.34, 'km': 1.60934, 'ft': 5280},
            'ft': {'m': 0.3048, 'km': 0.0003048, 'mi': 0.000189394}
        }

temp_conversion = {
            'c': {'f': lambda x: (x * 9/5) + 32, 'k': lambda x: x + 273.15},
            'f': {'c': lambda x: (x - 32) * 5/9, 'k': lambda x: (x - 32) * 5/9 + 273.15},
            'k': {'c': lambda x: x - 273.15, 'f': lambda x: (x - 273.15) * 9/5 + 32}
        }

def wt_change():
    while True:
        wt_unit_initial = input("Enter the unit of weight (kg/g/lb/oz): ")
        wt_unit_final = input("Enter the unit you wish to convert to (kg/g/lb/oz): ")
        wt_input = float(input("Enter the weight you wish to change: "))
        wt_output = wt_input * wt_conversion[wt_unit_initial.lower()][wt_unit_final.lower()]
        print(f"{wt_input} {wt_unit_initial} is equal to {wt_output} {wt_unit_final}")
        cont = input("Do you wish to continue in this mode(y/n): ")
        if cont.lower() == 'y':
            continue
        elif cont.lower() == 'n':
            break
        else:
            print("Invalid Value, Try again!!")


def dist_change():
    while True:
        dist_unit_initial = input("Enter the unit of distance (m/km/mi/ft): ")
        dist_unit_final = input("Enter the unit you wish to convert to (m/km/mi/ft): ")
        dist_input = float(input("Enter the distance you wish to change: "))
        dist_output = dist_input * dist_conversion[dist_unit_initial.lower()][dist_unit_final.lower()]
        print(f"{dist_input} {dist_unit_initial} is equal to {dist_output} {dist_unit_final}")
        cont = input("Do you wish to continue in this mode (y/n): ")
        if cont.lower() == 'y':
            continue
        elif cont.lower() == 'n':
            break
        else:
            print("Invalid Value, Try again!!")

def temp_change():
    while True:
        temp_unit_initial = input("Enter the unit of temperature (C/F/K): ")
        temp_unit_final = input("Enter the unit you wish to convert to (C/F/K): ")
        temp_input = float(input("Enter the temperature you wish to change: "))
        
        temp_output = temp_conversion[temp_unit_initial.lower()][temp_unit_final.lower()](temp_input)
        print(f"{temp_input} {temp_unit_initial} is equal to {temp_output} {temp_unit_final}")
        cont = input("Do you wish to continue in this mode (y/n): ")
        if cont.lower() == 'y':
            continue
        elif cont.lower() == 'n':
            break
        else:
            print("Invalid Value, Try again!!")

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
