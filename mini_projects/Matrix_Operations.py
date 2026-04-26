# INPUT A MATRIX
def input_matrix():
    while True:
        try:
            num_row = int(input("Num of rows: "))
            num_col = int(input("Num of columns: "))
            while num_row <= 0 or num_col <= 0:
                print("Number of rows and columns must be positive integers. Please try again.")
                num_row = int(input("Num of rows: "))
                num_col = int(input("Num of columns: "))
            matrix = []
            print("Enter the elements (space-separated):")
            for i in range(num_row):
                row = list(map(int, input().split()))
                while len(row) != num_col:
                    print("Invalid number of columns, please enter again.")
                    row = list(map(int, input().split()))
                matrix.append(row)
            return matrix
        except ValueError:
            print("Invalid input. Please enter integers only.")

# DISPLAY THE MATRIX
def display_matrix(matrix):
    print("Matrix:")
    for row in matrix:
        print(row,end="\n")

# ADDITION OF TWO MATRICES
def basic_operators(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        print("Invalid Matrix dimensions, should be the same for both matrices.")
        return None
    a = input("Enter mode (add/subtract/multiply): ").strip().lower()
    while a not in ['add', 'subtract','multiply']:
        print("Invalid input. Please enter 'add' or 'subtract' or 'multiply'.")
        a = input("Enter mode (add/subtract/multiply): ").strip().lower()
    result = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[0])):
            if a == 'add':
                row.append(matrix_1[i][j] + matrix_2[i][j])
            elif a == 'subtract':
                row.append(matrix_1[i][j] - matrix_2[i][j])
            elif a == 'multiply':
                row.append(matrix_1[i][j] * matrix_2[i][j])
        result.append(row)
    display_matrix(result)
    return result


# TRANSPOSE OF A MATRIX
def transpose_matrix(matrix):
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    display_matrix(result)
    return result

# MENU
def menu():
    print("--------------------------------------------------------")
    print("-------------- STARTING MATRIX OPERATIONS --------------")
    print("Available Operations:")
    print("1. Input Matrix & Display Matrix")
    print("2. Add/Subtract/Multiply Matrices")
    print("3. Transpose Matrix")
    print("4. Exit")
    while True:
        inp = int(input("Enter your choice (1/2/3/4): ").strip())
        match inp:
            case 1:
                matrix = input_matrix()
                display_matrix(matrix)
            case 2:
                print("Matrix 1:")
                matrix_1 = input_matrix()
                print("Matrix 2:")
                matrix_2 = input_matrix()
                basic_operators(matrix_1, matrix_2)
            case 3:
                print("Matrix:")
                matrix = input_matrix()
                transpose_matrix(matrix)
            case 4:
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please enter a valid option.")
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont == 'n':
            print("Exiting...")
            break
        if cont != 'y':
            print("Invalid input. Returning to menu.")
