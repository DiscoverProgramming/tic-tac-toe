# Tic Tac Toe Game

This is a simple Tic Tac Toe game implemented using Python's Tkinter library. The game features a basic graphical interface and AI opponent.

## Features

- 2-player mode: Play against the AI.
- AI opponent: The AI uses the Minimax algorithm with alpha-beta pruning to make optimal moves.
- Simple graphical interface using Tkinter.
- Win, lose, and tie detection.

## Prerequisites

- Python 3.x

## How to Run

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Save the code to a file named `tic_tac_toe.py`.

3. Run the script from the command line:
   ```
   python tic_tac_toe.py
   ```

## How to Play

- The game starts with an empty 3x3 grid.
- Player X always goes first.
- Players take turns clicking on empty cells to place their mark (X or O).
- The game will automatically detect a win, lose, or tie and display a message accordingly.

## Code Overview

- The game board is created using Tkinter's `Button` widget.
- The buttons are arranged in a 3x3 grid using the `grid` method.
- The Minimax algorithm with alpha-beta pruning is implemented to determine the best moves for the AI.
- The game logic handles player turns, move validation, and win/tie detection.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the Tkinter documentation and various online resources for guidance on using Tkinter.
