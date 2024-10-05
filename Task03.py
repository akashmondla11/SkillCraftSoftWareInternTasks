# Task 3 : create a program that solved Sudoku puzzles 
# (code written by Akash Mondal)
import tkinter as tk
from tkinter import messagebox
class SudokuSolverProject:
    def __init__(self, root):
        self.root = root
        self.root.title("SudokuSolverProject [By Akash Mondal]")
        self.root.configure(bg="grey")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.create_input_box()
        self.create_sudoku_buttons()
# i create  9*9 user input (we input values to solve a unlolved sudoku game)
    def create_input_box(self):
        for row in range(9):
            for col in range(9):
                e = tk.Entry(self.root, width=3, justify='center', font=('Arial', 18), borderwidth=1, bg="lightgrey")  # Set the background of the entries
                e.grid(row=row, column=col, padx=1, pady=1)
                self.cells[row][col] = e
#i create a solve and a clear buttons(we add solve button to solve the problem and we also add clear button to clear all input data)
    def create_sudoku_buttons(self):
        solvebutton = tk.Button(self.root, text="Solve", bg="green", fg="white", command=self.solvethepattern, font=('Arial', 15), width=10)
        solvebutton.grid(row=9, column=3, columnspan=3, pady=8)
        clearbutton = tk.Button(self.root, text="Clear", bg="darkred", fg="white", command=self.cleargridvalues, font=('Arial', 15), width=10)
        clearbutton.grid(row=11, column=3, columnspan=3, pady=8)  
#clear the input values taken from the user to solve the program
    def cleargridvalues(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
# read the user input data and store in array
    def readgridvalues(self):
        for row in range(9):
            for col in range(9):
                value = self.cells[row][col].get()
                if value.isdigit():
                    self.grid[row][col] = int(value)
                    
                else:
                    self.grid[row][col] = 0
# Check number is valid or not
    def isvalidornot(self, num, pos):
        row, col = pos
        for i in range(9):
            if self.grid[row][i] == num and col != i:
                return False
        for i in range(9):
            if self.grid[i][col] == num and row != i:
                return False
# 3*3 box Checking
        inputrow = row//3
        inputcol = col//3
        for i in range(inputrow*3,inputrow *3+3):
            for j in range(inputcol*3, inputcol*3+3):
                if self.grid[i][j]==num and(i,j)!=pos:
                    return False
        return True
#find an empty box's
    def emptycells(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return (row, col)  
                # row & col returned
        return None
#solved the sudoku problem give by the user (using the backtracking algorithm)
    def solve(self):
        empty = self.emptycells()
        if not empty:
            return True 
        row, col = empty
        for num in range(1, 10):
            if self.isvalidornot(num, (row, col)):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False
#display the sulution of it
    def sudokusolution(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(self.grid[row][col]))
    def solvethepattern(self):
        self.readgridvalues()
        if not self.solve():
            messagebox.showerror("error", "No result pliz try again")
        else:
            self.sudokusolution()
# main function 
def main():
    root = tk.Tk()
    app = SudokuSolverProject(root)
    root.mainloop()

if __name__ == "__main__":
    main()