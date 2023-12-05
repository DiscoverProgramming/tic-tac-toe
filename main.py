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
scores = {"X": -10, "O": 10, "tie": 0}

def minimax(board, depth, isMaximizing, alpha, beta):
    winner = check_win()
    if winner:
        return scores[winner]

    if isMaximizing:
        bestScore = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j]["text"] == "":
                    board[i][j]["text"] = "O"
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j]["text"] = ""
                    bestScore = max(score, bestScore)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j]["text"] == "":
                    board[i][j]["text"] = "X"
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j]["text"] = ""
                    bestScore = min(score, bestScore)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return bestScore

def button_click(row, col):
    global current_player, moves
    button = buttons[row][col]
    if button["text"] == "":
        button["text"] = current_player
        if current_player == "X":
            button.config(fg="red", font=("Arial", 9, "bold"))
            current_player = "O"
            moves += 1
            winner = check_win()
            if winner:
                show_win_screen(winner)
            elif moves < 9:
                bestScore = float('-inf')
                bestMove = None
                for i in range(3):
                    for j in range(3):
                        if buttons[i][j]["text"] == "":
                            buttons[i][j]["text"] = "O"
                            score = minimax(buttons, 0, False, float('-inf'), float('inf'))  # Add missing arguments
                            buttons[i][j]["text"] = ""
                            if score > bestScore:
                                bestScore = score
                                bestMove = (i, j)
                button_click(bestMove[0], bestMove[1])
        else:
            button.config(fg="blue", font=("Arial", 9, "bold"))
            current_player = "X"
            moves += 1
            winner = check_win()
            if winner:
                show_win_screen(winner)

def check_win():
    # Check rows
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]

    # Check columns
    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            return buttons[0][j]["text"]

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    # Check for a tie
    if all(button["text"] != "" for row in buttons for button in row):
        return "tie"

    return None

def show_win_screen(winner):
    if winner != "tie":
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
    else:
        messagebox.showinfo("Game Over", "It's a tie!")
    window.destroy()

# Bind button click event to the button_click function
for i in range(3):
    for j in range(3):
        buttons[i][j].config(command=lambda row=i, col=j: button_click(row, col))

# Start the main event loop
window.mainloop()