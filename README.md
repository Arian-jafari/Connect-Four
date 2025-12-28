# Connect Four with AI

A modern Connect Four game built in **Python** with **Pygame**, featuring multiple gameplay modes and intelligent AI strategies.

## Features

- **Multiple game modes**:
  - Human vs Human
  - Human vs AI
  - AI vs AI (watch the AI compete against itself)
- **AI Algorithms**:
  - Minimax
  - Alpha-Beta Pruning
  - Expectimax
- **Switchable board sizes**: 6×6 or 9×9
- **Interactive GUI**:
  - Smooth piece-dropping animations
  - Hover effects and clickable buttons
  - End game screen with restart/quit options
- **Win detection** for horizontal, vertical, and diagonal connections
- **Draw detection** if the board is full

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Arian-jafari/Connect-Four
cd Connect-Four

2. Install dependencies:
pip install requirements.txt

3. Run the game:
python main.py

## **Controls**

- Mouse movement: Move the piece indicator on top of the board
- Mouse click: Drop your piece in the selected column
- Menu buttons: Choose game mode, switch board size, restart, or quit

## **Project Structure**:
Connect-Four/
│── engine.py       # AI algorithms (Minimax, Alpha-Beta, Expectimax)
│── game.py         # Game logic (board, moves, win/draw detection)
│── gui.py          # Pygame GUI, menus, buttons, and animations
│── main.py         # Entry point to run the game
│── utils.py        # Board evaluation functions for AI
│── README.md       # Project documentation

