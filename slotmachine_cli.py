import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

COLS = 3
ROWS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6
}

symbol_value = {
    "A":4,
    "B":3,
    "C":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines

def slot_machine_spin(rows, cols, symbols):
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
                print(column[row], end="|")
            else:
                print(column[row], end="")
        print()                    

def deposit():
    while True:
        amount = input("Enter a amount you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount can't be less than 0.")
        else:
            print("The entered amount must be in number")
    return amount

def get_num_of_lines():
    while True:
        lines = input("Enter the num of lines you would like to bet on (1-" + str(MAX_LINES) + ") ?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("The entered lines must be in number")
    return lines

def get_bet():
    while True:
        amount = input("What amount would you like to bet on each lines? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The bet amount must be between ${MIN_BET}- ${MAX_BET}")
        else:
            print("The entered amount must be in number")
    return amount

def spin(balance):
    lines = get_num_of_lines()   
    while True:
        bet = get_bet()
        Total_bet = bet * lines
        if Total_bet > balance:
            print(f"You do not have enough balance to make this amount of bet. Your current balance is ${balance}")
        else:          
            break
    print(f"You are going to bet ${bet} on {lines} lines. Total bet is equal to: ${Total_bet}")
    
    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings( slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on: line", *winnings_lines)
    return winnings - Total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        play = input("Press enter to play or(q to quit).")
        if play == "q":
            break

        balance += spin(balance)
    print(f"You left with ${balance}")

main()