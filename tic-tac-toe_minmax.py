import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x300")
        self.board = [[None]*3 for _ in range(3)]
        self.player = 'X'
        self.opponent = 'O'
        self.empty_cells = 9
        for i in range(3):
            for j in range(3):
                self.board[i][j] = tk.Button(self.window, text=" ", font=('normal', 40, 'normal'), height=1, width=2, command=lambda i=i, j=j: self.make_move(i,j))
                self.board[i][j].grid(row=i, column=j)
        tk.Label(self.window, text="Player: X").grid(row=3)
        self.window.mainloop()

    def make_move(self, x, y):
        if self.board[x][y]['text'] == " ":
            self.board[x][y]['text'] = self.player
            self.empty_cells -= 1
            if self.check_win(self.player):
                messagebox.showinfo("Winner", "Player X wins!")
                self.window.destroy()
            elif not self.empty_cells:
                messagebox.showinfo("Tie", "It's a tie!")
                self.window.destroy()
            else:
                move = self.minimax(self.opponent)
                if move:
                    self.board[move[0]][move[1]]['text'] = self.opponent
                    if self.check_win(self.opponent):
                        messagebox.showinfo("Winner", "Player O wins!")
                        self.window.destroy()
                    else:
                        self.empty_cells -= 1

    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j]['text'] == player for j in range(3)):
                return True
            if all(self.board[j][i]['text'] == player for j in range(3)):
                return True
        if all(self.board[i][i]['text'] == player for i in range(3)):
            return True
        if all(self.board[i][2-i]['text'] == player for i in range(3)):
            return True
        return False

    def minimax(self, player):
        best_move = None
        best_score = float('-inf') if player == 'O' else float('inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j]['text'] == " ":
                    self.board[i][j]['text'] = player
                    score = self.minimax_score(player)
                    if (player == 'O' and score > best_score) or (player == 'X' and score < best_score):
                        best_score = score
                        best_move = (i,j)
                    self.board[i][j]['text'] = " "
        return best_move

    def minimax_score(self, player):
        if self.check_win('O'):
            return 10
        elif self.check_win('X'):
            return -10
        elif not any(self.board[i][j]['text'] == " " for i in range(3) for j in range(3)):
            return 0
        next_player = 'X' if player == 'O' else 'O'
        best_score = float('-inf') if next_player == 'O' else float('inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j]['text'] == " ":
                    self.board[i][j]['text'] = next_player
                    score = self.minimax_score(next_player)
                    if (next_player == 'O' and score > best_score) or (next_player == 'X' and score < best_score):
                        best_score = score
                    self.board[i][j]['text'] = " "
        return best_score

if __name__ == "__main__":
    TicTacToe()