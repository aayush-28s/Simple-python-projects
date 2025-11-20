import tkinter as tk
from tkinter import messagebox
import random
import time

root = tk.Tk()
root.title("Slot Machine")
root.resizable(width= False, height= False)
root.geometry("900x800")
root.configure(bg="#2d2d2d")

balance = 0
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

COLS = 3
ROWS = 3

symbol_count = {
    "🍎":3,
    "🥭":4,
    "🍇":6
}

symbol_value = {
    "🍎":5,
    "🥭":4,
    "🍇":3
}

balance_var = tk.StringVar()
balance_var.set("Balance : $0")

slot_result_var = tk.StringVar()
slot_result_var.set("")

win_var = tk.StringVar()
win_var.set("")

deposit_entry = tk.Entry(root)
lines_entry = tk.Entry(root)
bet_entry = tk.Entry(root)

def check_winnings(columns, selected_lines, bet, values):
    winning = 0
    winning_lines = []
    for line in selected_lines:
        symbol = columns[0][line - 1]
        for column in columns:
            if column[line - 1] != symbol:
                break
        else:
            winning += symbol_value[symbol] * bet
            winning_lines.append(line)
    return winning, winning_lines

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
    global balance
    amount = deposit_entry.get()
    if amount.isdigit() and int(amount)> 0:
        balance += int(amount)
        balance_var.set(f"Balance: ${balance}")
        deposit_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Enter a valid positive number")

def animate_reels(slots, step = 0, max_steps = 15):
    if step < max_steps:
        rows_display = []
        for row in range(ROWS):
            row_symbols = [random.choice(list(symbol_count.keys())) for _ in range(COLS)]
            rows_display.append("|".join(row_symbols))
        slot_result_var.set("\n".join(row_symbols))  
        root.after(100, lambda: animate_reels(slots, step + 1, max_steps))
    else:
        rows_display=[]
        for row in range(ROWS):
            row_symbols = [slots[col][row] for col in range(COLS)]
            rows_display.append("|".join(row_symbols))
            slot_result_var.set("\n".join(rows_display))

def reset_game():
    global balance
    balance = 0
    balance_var.set("Balance : $0")
    slot_result_var.set("")
    win_var.set("")
    deposit_entry.delete(0, tk.END)
    lines_entry.delete(0, tk.END)
    bet_entry.delete(0, tk.END)


def spin():
    global balance
    line_input = lines_entry.get().replace("","")
    bet = bet_entry.get()

    if not (bet.isdigit()):
        messagebox.showerror("Invalid Input", "lines and bet must be in numbers.")
        return
    
    try:
        selected_lines = list(map(int, line_input.split(",")))
    except:
        messagebox.showerror("Invalid Lines",f"Please enter rows as numbers, separated by commas.")
        return
    
    for line in selected_lines:
        if line < 1 or line > ROWS:
            messagebox.showerror("Invalid rows", f"Row {line} is invalid. Must be between 1 to {ROWS}") 
            return

    bet = int(bet)
 
    total_bet = len(selected_lines) * bet
    if total_bet > balance:
        messagebox.showwarning("Insufficient Balance", f"Your balance is ${balance}.")
        return
    
    balance -= total_bet
    slots = slot_machine_spin(ROWS, COLS, symbol_count)

    animate_reels(slots)

    root.after(1500, lambda: finish_spin(slots, selected_lines, bet))

def finish_spin(slots, lines, bet):
    global balance
    winning, winning_line = check_winnings(slots, lines, bet, symbol_value)
    balance += winning
    
    balance_var.set(f"Balance:${balance}")
    if winning > 0:
        win_var.set(f"You won ${winning} on lines: {','.join(map(str, winning_line))}")
    else:
        win_var.set("No winning this round.")

def make_label(master, text=None, textvariable=None, font=("Arial", 12), **kwargs):
    return tk.Label(master, text=text, textvariable=textvariable, font=font, fg="white", bg="#2d2d2d", **kwargs)

def make_button(master, text, command, **kwargs):
    return tk.Button(master, text=text, command=command, bg="#ffcc00", fg="black",
                     font=("Arial", 14, "bold"), activebackground="#ffaa00",width=10, height=1, **kwargs)

main_frame = tk.Frame(root, bg="#2d2d2d")
main_frame.pack(pady=20)

font_large = ("Arial", 16, "bold")
entry_font = ("Arial", 14)
entry_width = 30 

label_padding = (10,15)
entry_padding = (0,25)
button_padding = (0,25)
# Top Balance Display
make_label(main_frame, textvariable=balance_var, font=("Arial", 16, "bold")).pack(pady=label_padding)

# Deposit Section
make_label(main_frame, text="💰 Deposit Amount").pack(pady=label_padding)
deposit_entry = tk.Entry(main_frame, font= entry_font, width= entry_width, justify="center")
deposit_entry.pack(pady=entry_padding)
make_button(main_frame, text="Deposit", command=deposit).pack(pady=button_padding)

# Bet Section
make_label(main_frame, text="🎯 Enter Rows to Bet On (e.g. 1,2 or just 2)").pack(pady=label_padding)
lines_entry = tk.Entry(main_frame, font= entry_font, width= entry_width, justify="center")
lines_entry.pack(pady=entry_padding)

make_label(main_frame, text="🎲 Bet Per Line").pack(pady=label_padding)
bet_entry = tk.Entry(main_frame, font= entry_font, width= entry_width, justify="center")
bet_entry.pack(pady=entry_padding)

make_button(main_frame, text="🎰 Spin", command=spin).pack(pady=15)
make_button(main_frame, text="🔁 Reset", command=reset_game).pack(pady=10)

# Results Display
tk.Label(main_frame, textvariable=slot_result_var, font=("Courier", 20), fg="#00ff99", bg="#2d2d2d").pack(pady=15)
make_label(main_frame, textvariable=win_var, font=("Arial", 14)).pack(pady=5)


root.mainloop()

    