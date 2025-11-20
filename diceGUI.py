import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk
import pygame
import random 

# Load the images for dice faces
dice_images = [
    "dice1.png",
    "dice2.png",
    "dice3.png",
    "dice4.png",
    "dice5.png",
    "dice6.png"
]

# Creating a dice app window
class DiceApp(tk.Tk):
    def __init__(self):
        super().__init__() 

        self.title("Dice Simulator")
        self.geometry("800x600")

        # Create a dictionary to store pages
        self.frames = {}

        # Loop through and create both pages
        for Page in (HomePage, DicePage):
            frame = Page(self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_page(HomePage)
    
    def show_page(self, page_class):
        """Function to raise a frame (page)"""
        frame = self.frames[page_class]
        frame.tkraise()

# Home page
class HomePage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Load and resize background image
        self.bg_image = Image.open("dice7.jpg")
        self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)  # Store as an instance variable

        # Create Canvas for Full-Screen Background
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Add Widgets on Top of Canvas
        self.label = Label(self, text="Welcome to the Dice Simulator 🎲", font=("Arial", 20, "bold"), bg="black", fg = "white")
        self.label_window = self.canvas.create_window(400, 200, window=self.label)

        self.start_button = Button(self, text="Start the App", font=("Arial", 16), command=lambda: parent.show_page(DicePage))
        self.start_button_window = self.canvas.create_window(400, 300, window=self.start_button)

# Dice page
class DicePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Load dice images as tkinter PhotoImage objects
        self.dice_photos = [tk.PhotoImage(file=img) for img in dice_images]

        # Create and place widgets 
        self.dice_label = Label(self, image=self.dice_photos[0])
        self.dice_label.pack(pady=20)

        self.result_label = Label(self, text="Click to start", font=("Arial", 14))
        self.result_label.pack()
        
        roll_button = Button(self, text="Dice Roll 🎲", command=self.dice_roll, font=("Arial", 15), bg="pink", fg="red")
        roll_button.pack(pady=20)

        back_button = Button(self, text="Back to home", font=("Arial", 16), command=lambda: parent.show_page(HomePage))
        back_button.pack(pady=10)

    # Function to roll the dice 
    def dice_roll(self):
        """ Roll the dice with animation effect. """
        self.roll_count = 10  # Number of rolling frames
        self.animate_roll()

    def animate_roll(self):
        """ Animate the dice roll before stopping at the final value. """
        if self.roll_count > 0:
            # Pick a random dice image during the rolling effect
            random_dice = random.randint(0, 5)
            self.dice_label.config(image=self.dice_photos[random_dice])
            self.roll_count -= 1
            self.after(100, self.animate_roll)  # Delay animation (100ms)
        else:
            # Final roll result after animation stops
            final_value = random.randint(1, 6)
            self.dice_label.config(image=self.dice_photos[final_value - 1])
            self.result_label.config(text=f"You rolled a {final_value}!")

if __name__ == "__main__":
    app = DiceApp()
    app.resizable(False, False)
    app.mainloop()
