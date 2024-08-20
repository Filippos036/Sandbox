import random

while True:
    dice_roll = int(input("Type 1 to roll the dice, type 2 to end the program: "))
    
    if dice_roll == 1:
        roll_result = random.randint(1, 6)
        print(f"Wow, you rolled a {roll_result}!")
    elif dice_roll == 2:
        print("Goodbye!!!")
        break  
    else:
        print(":( wrong input!!! try again")
