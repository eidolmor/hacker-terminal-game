# Hacker Terminal Game

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Project%20Demo-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A terminal-based cybersecurity simulation game built in Python.  
Play as an ethical hacker and complete missions involving password cracking, encryption, and log analysis.

## Features

- **Password Cracking** — Use terminal commands like `scan`, `hint`, and `login` to discover a randomized password.
- **Cipher Decryption** — Decode Caesar cipher messages with dynamic shifts and smart hints.
- **Log Analysis** — Inspect realistic system logs to detect suspicious users or IP activity.
- **Difficulty Levels** — Choose from Easy, Medium, or Hard.
- **Score System** — Earn points across 3 missions for a total of 30 points.
- **Replayable Gameplay** — Every run generates fresh challenges.
- **Terminal Effects** — ASCII banner and slow-printing output for a realistic terminal feel.

## Gameplay

1. Select a difficulty level.
2. Complete 3 missions:
   - Crack the password.
   - Decrypt the cipher.
   - Analyze logs.
3. Earn a score based on your performance.
4. Replay and try again with new randomized challenges.

## Concepts Used

- Python fundamentals: loops, conditionals, and functions
- Modular programming with multiple files
- Object-Oriented Programming with a `Game` class
- Randomization for challenge generation
- Basic cybersecurity concepts

## Project Structure

```bash
hacker-terminal-game/
│
├── main.py          # Game flow and control (Game class)
├── challenges.py    # All missions (password, cipher, logs)
├── utils.py         # Helper functions (UI, difficulty, printing)
└── README.md
```

## Requirements

- Python 3.10 or higher
- A terminal or command prompt
- No external packages required

## How to Run

1. Clone the repository or download the project files.
2. Open a terminal in the project folder.
3. Run the game:

```bash
python main.py
```

## Example Output

```text
====================================
   HACKER TERMINAL GAME
====================================

Choose difficulty: Easy / Medium / Hard
Mission 1: Crack the password
Mission 2: Decrypt the cipher
Mission 3: Analyze the logs
```

## Future Improvements

### Logging System
Track player actions, attempts, and performance.

### Web-Based Version
Convert the game into a browser-based version using Flask or Django.

### More Missions
Add new challenges such as:
- Brute force simulation
- SQL injection puzzles
- Network scanning

### AI-Based Hints
Create adaptive hints based on player behavior.

### Save Progress
Allow players to resume from their last mission.

### Enhanced UI
Add colors, animations, and richer terminal effects.

## Author

**EIDOLMOR**

## Conclusion

This project demonstrates how basic Python concepts can be used to build an interactive and educational cybersecurity simulation. It balances simplicity with engaging gameplay and provides a foundation for more advanced features in the future.