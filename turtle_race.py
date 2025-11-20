import turtle
import time
import random
import tkinter as tk
from tkinter import messagebox

WIDTH , HEIGHT = 700, 600
COLORS = ["RED", "BLUE", "GREEN", "YELLOW", "BROWN", "PINK", "VIOLET","CYAN", "OLIVE", "PURPLE"]


def race(colors):
    turtles = creating_turtle(colors)
    while True:
        for racer in turtles:
            speed = random.randrange(1,20)
            racer.forward(speed)

            x,y = racer.pos()
            if y >= HEIGHT//2 - 15:
                return colors[turtles.index(racer)]

def creating_turtle(colors):
    turtles = []
    spacingx = WIDTH// (len(colors) +1)
    for i, color in enumerate(colors):   
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def start_race():
    try:
        racers = int(entry.get())
        if not (2 <= racers <= 10):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number between (2 - 10)")
        return
    
    root.withdraw()

    turtle.clearscreen()
    turtle.setup(WIDTH, HEIGHT)
    turtle.title("Turtle Race !")

    random.shuffle(COLORS) 
    colors = COLORS[:racers] 
    winner = race(colors)

    messagebox.showinfo("🏁 Race Finished", f"The winner is the {winner.upper()} turtle!")
    turtle.bye()
    root.deiconify()

root = tk.Tk()
root.title("Turtle_Race")
root.geometry("400x400")
root.configure(bg="#222222")

tk.Label(root, text="Turtle Race Game", font=("Arial", 16, "bold"), bg="#222222", fg="white").pack(pady=10)
tk.Label(root, text="Enter number of racers between (2–10):", font=("Arial", 12), bg="#222222", fg="white").pack(pady=15)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=10)

start_btn = tk.Button(root, text="Start Race", font=("Arial", 12, "bold"), command=start_race, bg="#00cc66", fg="white")
start_btn.pack(pady=10)

root.mainloop()
