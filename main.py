import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9
        for i in range(9):
            button = tk.Button(self.window, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.update_button_text(index)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    def update_button_text(self, index):
        button = self.window.winfo_children()[index]
        button.config(text=self.board[index])
    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return self.board[combo[0]]
        return None
    def reset_board(self):
        self.board = [""] * 9
        for button in self.window.winfo_children():
            button.config(text="")
        self.current_player = "X"
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
