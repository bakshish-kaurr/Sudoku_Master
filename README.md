# Sudoku Master

## Overview

Sudoku Master is a comprehensive, Python-based application to play and solve Sudoku puzzles in both 4x4 and 9x9 formats. Designed with students, puzzle enthusiasts, and aspiring programmers in mind, this Tkinter-driven GUI project demonstrates the application of recursive backtracking algorithms, interactive GUI design, and modular code architecture.

## Features

- **Dual Modes:** Play Sudoku puzzles in either 4x4 or 9x9 grids, with seamless switching from the menu.
- **Difficulty Levels:** Choose Easy, Medium, or Hard to set the challenge for your Sudoku puzzle.
- **User-Friendly GUI:** Clean, clickable interface—select cells, fill numbers, and interact with game options effortlessly.
- **Assistance Tools:** Integrated hints, undo, show solution, and puzzle reset for learning and convenience.
- **Backtracking Solver:** Built-in solver validates solutions and generates puzzles with guaranteed solvability.
- **Educational Value:** Great demonstration of recursion, array handling, GUI event management, and algorithmic thinking.

## Getting Started

1. Ensure that Python 3.x is installed on your system (plus Tkinter, which is included in Python Standard Library).
2. Place all provided `.py` files in a folder.
3. To start the application, run: `python main_menu.py`

4. Choose either the 4x4 or 9x9 mode from the GUI. Experiment with different difficulty levels and features.

## Project Structure

| Filename        | Description                                    |
|-----------------|------------------------------------------------|
| main_menu.py    | Launches the main menu and controls navigation |
| sudoku_4x4.py   | Logic, rules, and GUI for 4x4 Sudoku          |
| sudoku_9x9.py   | Logic, rules, and GUI for 9x9 Sudoku          |
| image.jpg       | (optional) screenshot or branding asset        |

## Technical Details

- **Algorithms:** The puzzle solver and generator rely on depth-first search and backtracking to fill the grid, avoiding duplicate solutions and unsolvable states.
- **Data Structures:** 2D arrays represent the Sudoku grid, supporting efficient state updates and validations.
- **GUI Events:** Tkinter handles cell selection, button clicks, puzzle resets, difficulty selection, and solution display seamlessly.
- **Modular Design:** Each module (menu, 4x4 game, 9x9 game) is self-contained, ensuring readability and ease of future expansion.

## Learning Outcomes

- Understand, implement, and optimize recursive and backtracking algorithms in the context of Sudoku.
- Learn principles of GUI application development with Python's Tkinter.
- Practice designing maintainable, modular Python code for real-world projects.
- Develop problem-solving and debugging skills in a fun, interactive way.

## Credits

Developed by `Bakshish Kaur`. Inspired by popular Sudoku games, educational algorithm examples, and open-source Python projects. Thanks to the Python and puzzle communities for foundational concepts and resources.


