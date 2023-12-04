import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the game board
board = tk.Frame(window)
board.pack()

# Create the buttons for the game board
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(board, width=10, height=5)
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Game logic
current_player = "X"
moves = 0

def button_click(row, col):
    global current_player, moves
    button = buttons[row][col]
    if button["text"] == "":
        button["text"] = current_player
        if current_player == "X":
            button.config(fg="red", font=("Arial", 9, "bold"))
            current_player = "O"
        else:
            button.config(fg="blue", font=("Arial", 9, "bold"))
            current_player = "X"
        moves += 1
        check_win()

def check_win():
    # Check rows
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            show_win_screen(buttons[i][0]["text"])
            return

    # Check columns
    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            show_win_screen(buttons[0][j]["text"])
            return

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        show_win_screen(buttons[0][0]["text"])
        return

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        show_win_screen(buttons[0][2]["text"])
        return

    # Check for a tie
    if moves == 9:
        show_tie_screen()
        return

def show_win_screen(winner):
    messagebox.showinfo("Game Over", f"Player {winner} wins!")
    window.destroy()

def show_tie_screen():
    messagebox.showinfo("Game Over", "It's a tie!")
    window.destroy()

# Bind button click event to the button_click function
for i in range(3):
    for j in range(3):
        buttons[i][j].config(command=lambda row=i, col=j: button_click(row, col))

# Start the main event loop
window.mainloop()
