from tkinter import *

class Application(Frame):

     def __init__(self, master):
         super(Application,self).__init__(master)
         self.task=""
         self.UserIn = StringVar()
         self.grid()
         self.create_widgets()

     def create_widgets(self):
         self.user_input = Entry(self, bg="white", bd=30,insertwidth=5,width=18,
         font = ("Verdana", 20,"bold"), textvariable=self.UserIn,justify=RIGHT)
         self.user_input.grid(columnspan=4,rowspan=2, sticky=W)

         self.user_input.insert(0, "0")

         self.create_button(7, 3, 0, sticky=W)
         self.create_button(8, 3, 1, sticky=W)
         self.create_button(9, 3, 2, sticky=W)
         self.create_button(4, 4, 0, sticky=W)
         self.create_button(5, 4, 1, sticky=W)
         self.create_button(6, 4, 2, sticky=W)
         self.create_button(1, 5, 0, sticky=W)
         self.create_button(2, 5, 1, sticky=W)
         self.create_button(3, 5, 2, sticky=W)
         self.create_button(0, 6, 1, sticky=W)
         self.create_button('00', 6, 0, sticky=W)

         self.create_button('.', 6, 2, sticky=W)
         self.create_button('+', 5, 3, sticky=W)
         self.create_button('-', 4, 3, sticky=W)
         self.create_button('*', 3, 3, sticky=W)
         self.create_button('/', 2, 3, sticky=W)
         self.create_button('%', 2, 2, sticky=W)

         self.create_button('=', 6, 3, sticky=W, command=self.CalculateTask)
         self.create_button('AC', 2, 0, sticky=W, command=self.ClearDisplay)
         self.create_button('%', 2, 2, sticky=W)
    
     def create_button(self, text, row, col,sticky, command=None):
        if command is None:
            command = lambda t=text: self.button(t)
        button = Canvas(self, width=80, height=80, bg="white", highlightthickness=0)
        button.create_oval(10, 10, 70, 70, fill="black")
        button.create_text(40, 40, text=text, fill="white", font=("Helvetica", 25, "bold"))
        button.grid(row=row, column=col, padx=5, pady=5)
        button.bind("<Button-1>", lambda e, t=text: command())

     def button(self, number):
         self.task = str(self.task) + str(number)
         self.UserIn.set(self.task)

     def CalculateTask(self):
         self.data = self.user_input.get()
         try:
             self.answer = eval(self.data)
             self.displayText(self.answer)
             self.task = self.answer
         except Exception as e:
             self.displayText("Invalid Syntax")
             self.task = ""

     def displayText(self, value):
         self.user_input.delete(0, END)
         self.user_input.insert(0, str(value))

     def ClearDisplay(self):
         self.task = ""
         self.user_input.delete(0, END)
         self.user_input.insert(0, "0")


calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)

calculator.resizable(width= True, height= True)

calculator.mainloop()


