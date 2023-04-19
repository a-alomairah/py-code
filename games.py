import tkinter as tk
from tkinter import ttk
import random

# function to play Tic Tac Toe game
def play_tic_tac_toe():
    # initialize game state
    game_state = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    # function to draw the game board
    def draw_board():
        for row in game_state:
            print("|" + "|".join(row) + "|")

    # function to check if a player has won
    def has_won(player):
        # check rows
        for row in game_state:
            if all(cell == player for cell in row):
                return True

        # check columns
        for col in range(3):
            if all(game_state[row][col] == player for row in range(3)):
                return True

        # check diagonals
        if all(game_state[i][i] == player for i in range(3)):
            return True
        if all(game_state[i][2 - i] == player for i in range(3)):
            return True

        return False

    # function to handle a player's turn
    def player_turn(player):
        nonlocal current_player

        # prompt player for move
        move = input(f"{player}, enter your move (row column): ")
        row, col = map(int, move.split())

        # make move if valid
        if 0 <= row < 3 and 0 <= col < 3 and game_state[row][col] == " ":
            game_state[row][col] = player
            current_player = "X" if current_player == "O" else "O"
        else:
            print("Invalid move")

    # main game loop
    while True:
        draw_board()
        player_turn(current_player)

        if has_won("X"):
            draw_board()
            print("X wins!")
            break
        elif has_won("O"):
            draw_board()
            print("O wins!")
            break

# function to play Rock Paper Scissors game
def play_rock_paper_scissors():
    # code for Rock Paper Scissors game
    pass

# function to play Heads or Tails game
def play_heads_or_tails():
    # create list of options
    options = ["heads", "tails"]
    
    # generate random choice
    computer_choice = random.choice(options)
    
    # return computer choice
    return computer_choice

# create main window
root = tk.Tk()
root.title("Games")

# create tabs
notebook = ttk.Notebook(root)

# add Tic Tac Toe tab
tic_tac_toe_frame = ttk.Frame(notebook)
notebook.add(tic_tac_toe_frame, text="Tic Tac Toe")
tic_tac_toe_button = tk.Button(tic_tac_toe_frame, text="Play Tic Tac Toe", command=play_tic_tac_toe)
tic_tac_toe_button.pack()

# add Rock Paper Scissors tab
rock_paper_scissors_frame = ttk.Frame(notebook)
notebook.add(rock_paper_scissors_frame, text="Rock Paper Scissors")
rock_paper_scissors_button = tk.Button(rock_paper_scissors_frame, text="Play Rock Paper Scissors", command=play_rock_paper_scissors)
rock_paper_scissors_button.pack()

# add Heads or Tails tab
heads_or_tails_frame = ttk.Frame(notebook)
notebook.add(heads_or_tails_frame, text="Heads or Tails")
heads_or_tails_button = tk.Button(heads_or_tails_frame, text="Play Heads or Tails", command=play_heads_or_tails)
heads_or_tails_button.pack()

# add Play Again button to Heads or Tails tab
def play_again():
    result_label.config(text="")
    heads_or_tails_button.config(state=tk.NORMAL)
    play_again_button.pack_forget()
play_again_button = tk.Button(heads_or_tails_frame, text="Play Again", command=play_again)
play_again_button.pack_forget()

# create label to display result
result_label = tk.Label(heads_or_tails_frame, text="")
result_label.pack()

# function to play Heads or Tails game and update GUI
def play_heads_or_tails_gui():
    result = play_heads_or_tails()
    if result == "heads":
        result_label.config(text="Heads")
    else:
        result_label.config(text="Tails")
    heads_or_tails_button.config(state=tk.DISABLED)
    play_again_button.pack()

# configure button to play Heads or Tails game with GUI
heads_or_tails_button.config(command=play_heads_or_tails_gui)

notebook.pack(expand=True, fill="both")

# run main loop
root.mainloop()
