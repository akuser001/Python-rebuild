import random
row1 =  {1: "_ _", 2: "_ _", 3: "_ _"}
row2 = {4: "_ _", 5: "_ _", 6: "_ _"}
row3 = {7: "_ _", 8: "_ _", 9: "_ _"}
grid = { 1: row1,
        2: row2,
        3: row3}
elements = []
for row in grid:
    for cell in grid[row].values():
        elements.append(cell)

def display_grid(elements):
    for i in range(0,9,3):
        for j in range(3):
            print(elements[i+j], end="|")
        print()

empty_blocks = [0,1,2,3,4,5,6,7,8]
def user_turn(elements, empty_blocks):
    print("Your Turn!!")
    user_block = int(input("Enter the grid number: "))
    user_block -= 1
    if user_block in empty_blocks:
        empty_blocks.remove(user_block)
        elements[user_block] = "_x_"
    else:
        print(f"{user_block+1} is already filled, try again")
        user_block = int(input("Enter the grid number: "))
    display_grid(elements)

def pc_turn(elements, empty_blocks):
    print("PC's Turn!!")
    pc_block = random.choice(empty_blocks)
    print(f"PC chose {pc_block+1} block")
    empty_blocks.remove(pc_block)
    elements[pc_block] = "_o_"
    display_grid(elements)
win_combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def win_check(win_combos, elements):
    for win_combo_tuple in win_combos:
        if win_combo_tuple[0] == "_x_" and win_combo_tuple[1] == "_x_" and win_combo_tuple[2] == "_x_":
            print("You Won!!")
            break
        elif win_combo_tuple[0] == "_o_" and win_combo_tuple[1] == "_o_" and win_combo_tuple[2] == "_o_":
            print("Pc Won!!")
            break

def main():
    print("Welcome to game")
    print("The following is the values assigned for xo-grid while playing")
    for i in range(1,4):
        print(grid[i])
    print("All the best for your game!!")
    display_grid(elements)
    while True:
        while True:
            user_turn(elements,empty_blocks)
            if len(empty_blocks) == 0:
                print("It's a tie!")
                print("Game Over!!")
                break
            win_check(win_combos, elements)
            pc_turn(elements,empty_blocks)
            win_check(win_combos, elements)
        continue_game = input("Do you want to play again? (yes/no): ")
        if continue_game.lower() == "yes":  
            main()
        else:
            print("Thanks for playing! Goodbye!")
            print("Returning to main menu...")
            break