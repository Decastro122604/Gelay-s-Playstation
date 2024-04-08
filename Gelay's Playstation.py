import random
import os
import time 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1 

ROWS = 3
COLS = 3 

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
} 

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) 

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) 

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value) 

        columns.append(column) 

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="") 

        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.") 

    return amount

def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.") 

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.") 

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines 

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break 

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}") 

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance) 

    print(f"You left with ${balance}")

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

# Rock Paper Scissors game
def play_rps():
    clear_screen()
    print("Welcome to Rock Paper Scissors!\n")
    choices = ['rock', 'paper', 'scissors']
    while True:
        print("Choose your weapon:")
        for idx, choice in enumerate(choices, 1):
            print(f"{idx}. {choice}")
        print("0. Back to main menu")
        user_choice = input("Enter your choice: ").lower()
        if user_choice == '0':
            break
        elif user_choice not in choices:
            print("Invalid choice! Please enter a valid option.")
            continue
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")
        print()
        time.sleep(2) 

# Simple Snake game
def play_snake():
    clear_screen()
    items = ['apple', 'chicken', 'bugs', 'rock', 'rat', 'ant', 'frog', 'lizard', 'bunny', 'nothing']
    snake_eaten = random.choice(items)
    attempts = 3 

    print("Welcome to the Snake's Meal Guessing Game!")
    print("The snake has eaten something. Can you guess what it is? You have 3 attempts.")
    print("It might have been an apple, chicken, bugs, rock, rat, ant, frog, lizard, bunny or simply nothing") 

    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        if guess == snake_eaten:
            print("Congratulations! You guessed correctly!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect! Try again. You have {} attempts left.".format(attempts))
            else:
                print("Sorry, you're out of attempts! The snake has eaten {}.".format(snake_eaten))
                return

# Dice Roller game
def roll_dice():
    clear_screen()
    print("Welcome to Dice Roller!\n")
    while True:
        sides = input("Enter the number of sides for the dice (or 'q' to quit): ")
        if sides.lower() == 'q':
            break
        try:
            sides = int(sides)
            if sides <= 0:
                raise ValueError
            print(f"\nYou rolled: {random.randint(1, sides)}\n")
        except ValueError:
            print("Invalid input! Please enter a positive integer.\n")
        time.sleep(2) 

# Slot Machine game
def play_slot_machine():
    clear_screen()
    print("Welcome to the Slot Machine game!\n")
    main()

# Main menu
def main_menu():
    while True:
        clear_screen()
        print("Welcome to Gelay's PlayStation!")
        print("\n1. Rock Paper Scissors")
        print("2. Simple Snake")
        print("3. Dice Roller")
        print("4. Slot Machine")
        print("5. Quit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            play_rps()
        elif choice == '2':
            play_snake()
        elif choice == '3':
            roll_dice()
        elif choice == '4':
            play_slot_machine()
        elif choice == '5':
            print("\nThanks for playing! ")
            break
        else:
            print("\nInvalid choice! Please enter a number from 1 to 5.\n")
        time.sleep(2)

if __name__ == "__main__":
    main_menu()
