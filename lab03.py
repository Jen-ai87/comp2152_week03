# Lab 03 solutions

import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

# 1. Using list() and range()
diceOptions = list(range(1, 7))
print(diceOptions)


weapons = ["First", "Knife", "Club", "Gun", "Nuclear Bomb"]
print("Available weapons")

# 2. Use a for loop with the in keyword to iterate over the weapons array
i = 1
for w in weapons:
    print(f"{i}. {w}")
    i += 1

# 3. Player Input Validation

# Keep asking th player till the provide valid input
while True:
    try:
        combatStrength = int(input("Enter your combat Strength (Number between 1-6): "))
        # Check if the input is within the valid range
        if 1 <= combatStrength <= 6:
            break
        else:
            print("Error: Please enter a number between 1 and 6.")
    except ValueError:
        # Handle if input value is not an integer
        print("Error: Invalid input. Please enter an integer between 1 and 6.")

while True:
    try:
        # Get monster combat strength from the user
        mCombatStrength = int(input("Enter the monster's combat Strength (1-6): "))

        # Check if the input is within the valid range
        if 1 <= mCombatStrength <= 6:
            break
        else:
            print("Error: Please enter a number between 1 and 6.")
    except ValueError:
        # Handle if input value is not an integer
        print("Error: Invalid input. Please enter an integer between 1 and 6.")

# 4. Battle Sequence - 10 rounds with stepping by 2
for round_num in range(1, 21, 2):
    # Check for Battle Truce
    if round_num == 11:
        print(f"Battle Truce declared in Round {round_num}. Game Over!")
        break

    # Roll dice for hero and monster
    hero_roll = random.choice(diceOptions)
    monster_roll = random.choice(diceOptions)

    # Add dice roll to combat strength
    combatStrength += hero_roll
    mCombatStrength += monster_roll

    # Select weapon based on the dice roll
    hero_weapon = random.choice(weapons)
    monster_weapon = random.choice(weapons)

    # Add dice roll to combat strength
    hero_total_strength = combatStrength + hero_roll
    monster_total_strength = mCombatStrength + monster_roll
    print(f"Round {round_num}: Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {hero_total_strength}, Monster Total Strength: {monster_total_strength}.")

    # Determine the winner of the round
    if hero_total_strength > monster_total_strength:
        print("Hero wins the round!")
    elif hero_total_strength < monster_total_strength:
        print("Monster wins the round!")
    else:
        print("It's a tie!")

    print(" ")
