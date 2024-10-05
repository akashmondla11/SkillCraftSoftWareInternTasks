# Task 2 : create a program that generates a random number tha user can guess
# and user takes 5 attempt's only to guess 
# (code written by Akash Mondal)
import random
import tkinter as tk
class NumberGuessProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("NumberGuessProject[By Akash Mondal]")
        self.window.geometry("560x200")
        self.window.configure(bg="darkgreen")
        self.max_try = 5
        self.ClearGuessInputValue = self.max_try
# i set default range in the select range menu
        self.GuessRangeValue = tk.IntVar()
        self.GuessRangeValue.set(100)  
# default to 1-100
# i add Frame for range menu
        self.Range_f = tk.Frame(self.window, bg="darkgreen")
        self.Range_f.pack(pady=8)
# select guessing range (from the guess box)
        self.Range_select = tk.Label(self.Range_f, text="Select Range:", font=("Arial", 14), bg="darkgreen", fg="white")
        self.select_menu = tk.OptionMenu(self.Range_f, self.GuessRangeValue, 10, 100, 1000, command=self.Rangeset)
        self.select_menu.config(font=("Arial", 12), bg="green")  # Set background color to green
        self.Range_select.grid(row=0, column=0, padx=5)
        self.select_menu.grid(row=0, column=1, padx=5)
        self.Ran_num = random.randint(1, self.GuessRangeValue.get())
# Guess input Frame
        self.GuessFrame = tk.Frame(self.window, bg="darkgreen")
        self.GuessFrame.pack(pady=10)
        self.GuessLable = tk.Label(self.GuessFrame, text="Guess the number:", font=("Arial", 14), bg="darkgreen", fg="white")
        self.guessInputEntry = tk.Entry(self.GuessFrame, font=("Arial", 12), bg="lightgreen")  # Set background color to light green
        self.Placeholder_tx = f"Range: 1 to {self.GuessRangeValue.get()}"
        self.guessInputEntry.insert(0, self.Placeholder_tx)  # Add placeholder in the input box
        self.guessInputEntry.bind("<FocusIn>", self.remove_Placeholdr)
        self.guessInputEntry.bind("<FocusOut>", self.AddPlaceholder)
        self.guessattemptsLable = tk.Label(self.GuessFrame, text=f"Attempts left: {self.ClearGuessInputValue}", font=("Arial", 12), bg="darkgreen", fg="white")
        self.GuessLable.grid(row=0, column=0, padx=5)
        self.guessInputEntry.grid(row=0, column=1, padx=5)
        self.guessattemptsLable.grid(row=0, column=2, padx=5)
 #FeedbackLabel(in the next line))
        self.FeedbackLable = tk.Label(self.window, text="", font=("Arial", 12), bg="darkgreen", fg="white")
        self.FeedbackLable.pack(pady=5)
# Buttons frame 
        self.ButtonFrame = tk.Frame(self.window, bg="darkgreen")
        self.ButtonFrame.pack(pady=10)
# Buttons (Clear button and guess button)
        self.GuessButton = tk.Button(self.ButtonFrame, text="Guess", command=self.NumberGuessCheck, font=("Arial", 12), bg="green", fg="white", width=10)
        self.ClearButton = tk.Button(self.ButtonFrame, text="Clear", command=self.ClearGuessInputValue, state="disabled", font=("Arial", 12), bg="darkred", fg="white", width=10)
        self.GuessButton.grid(row=0, column=0, padx=5)
        self.ClearButton.grid(row=0, column=1, padx=5)
        self.window.bind('<Return>', self.EntryPass)
# Clear placeholder text when user the enterd the input box
    def remove_Placeholdr(self, event):
        if self.guessInputEntry.get() == self.Placeholder_tx:
            self.guessInputEntry.delete(0, tk.END)
# Add placeholder text if the user did not enter the input box or make it empty
    def AddPlaceholder(self, event):
        if self.guessInputEntry.get() == "":
            self.guessInputEntry.insert(0, self.Placeholder_tx)
# force NumberGuessCheck when enter key is pressed
    def EntryPass(self, event):
        self.NumberGuessCheck()
# update the game when user change the range selection from the range menu
    def Rangeset(self, _):
        self.Ran_num = random.randint(1, self.GuessRangeValue.get())
        self.GuessLable.config(text="Guess the number:")
        self.guessInputEntry.delete(0, tk.END)
        self.Placeholder_tx = f"Range: 1 to {self.GuessRangeValue.get()}"
        self.guessInputEntry.insert(0, self.Placeholder_tx)
        self.ClearGuessInputValue = self.max_try
        self.guessattemptsLable.config(text=f"Attempts left: {self.ClearGuessInputValue}")
        self.FeedbackLable.config(text="")
        self.GuessButton.config(state="normal")
        self.ClearButton.config(state="disabled")
        
    def NumberGuessCheck(self):
        try:
# Valid input and ignore placeholder_tx
            if self.ClearGuessInputValue > 0:
                user_input = self.guessInputEntry.get()
                if user_input == self.Placeholder_tx:
                    self.FeedbackLable.config(text="Please enter a valid guess!")
                    return
                user_guess = int(user_input)
                self.ClearGuessInputValue -= 1
                self.guessattemptsLable.config(text=f"Attempts left: {self.ClearGuessInputValue}")
                if user_guess != self.Ran_num:
                    if self.ClearGuessInputValue > 0:
                        self.FeedbackLable.config(text="Try again!")
                    else:
                        self.FeedbackLable.config(text="No more attempts left! You lost.")
                        self.GuessButton.config(state="disabled")
                        self.ClearButton.config(state="normal")
                else:
                    self.FeedbackLable.config(text="Correct! You guessed the number!")
                    self.GuessButton.config(state="disabled")
                    self.ClearButton.config(state="normal")
            else:
                self.FeedbackLable.config(text="No more attempts left! You lost.")
                self.GuessButton.config(state="disabled")
                self.ClearButton.config(state="normal")
        except ValueError:
            self.FeedbackLable.config(text="Invalid number pliz try again bro!") 
# Clear\Reset the game state (by clicking clear button)and reset\clean all values
    def ClearGuessInputValue(self):
        self.Ran_num = random.randint(1, self.GuessRangeValue.get())
        self.GuessLable.config(text="Guess the number:")
        self.guessInputEntry.delete(0, tk.END)
        self.Placeholder_tx = f"Range: 1 to {self.GuessRangeValue.get()}"
        self.guessInputEntry.insert(0, self.Placeholder_tx)  # Reset placeholder in the input box
        self.ClearGuessInputValue = self.max_try
        self.guessattemptsLable.config(text=f"Attempts left: {self.ClearGuessInputValue}")
        self.FeedbackLable.config(text="")
        self.GuessButton.config(state="normal")
        self.ClearButton.config(state="disabled")
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = NumberGuessProgram()
    game.run()
