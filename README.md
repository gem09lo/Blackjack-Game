### 🃏 Blackjack Game (Python CLI Project)

## 📖 Overview
This is a command-line Blackjack game developed as part of the Week 1 Python Fundamentals module during the Sigma Labs Data Engineering program.

The project uses procedural Python and includes clean code principles, test-driven development (TDD), and code quality best practices. It provides a simplified single-player version of Blackjack (player vs dealer) and serves as an early demonstration of software engineering fundamentals like version control, automated testing, and Pylint compliance.

## 🎯 Project Aims
- Build a working CLI Blackjack game using core Python.

- Practice test-driven development (TDD) with `pytest`.

- Follow clean code principles (e.g., readability, naming, single responsibility).

- Structure a Python project using modules and maintainable test files.

- Prepare code for code reviews using Pylint and automated testing.


## 🗂️ Project Structure

blackjack/
├── `blackjack.py`: Main game logic
├── support/
│   └── `testing_util.py`: Support functions for unit testing
├── `test_blackjack_coaches.py`: Coach-provided test cases
└── `test_blackjack_trainees.py`: Developer-written test cases

tdd_prototype/ (Optional) TDD practice folder
├── `generate_card.py`: Initial TDD implementation for card logic
└── `test_generate_card.py`: Unit tests for card logic

`README.md`: Project documentation
`requirements.txt`: Python dependencies
`.gitignore`: Git ignore rules

## ⚙️ Getting Setup
1. Clone the Repo:
   - `git clone https://github.com/your-username/blackjack-game.git`
   - `cd blackjack-game`
2. Set Up a Virtual Environment (Optional but Recommended)
   - `python -m venv .venv`
   - `source .venv/bin/activate`
3. Install Dependencies:
   - `pip install -r requirements.txt`
4. Run the Game:
   - `python blackjack/blackjack.py`
5. Run Tests:
   - `pytest blackjack/`

## 🧪 Testing
The game includes unit tests written with pytest. Some test cases were provided by coaches, and additional tests were written during development to support TDD. Utility functions used in testing are stored in `support/testing_util.py`.

## 📏 Code Quality
This project adheres to Python best practices using:

- **Pylint** for style and linting (minimum score target: 9.5/10).

- **pytest** for automated unit testing.

- **Clean code conventions**: meaningful naming, modular functions, readable logic.


## 🧠 What I Learned
- Writing procedural Python in a structured and modular way.

- Using test-driven development to build features incrementally.

- Applying Git version control and ignoring unnecessary files.

- Reading Pylint output to improve code quality and readability.

- Creating and interpreting pytest assertions to validate logic.


## 📎 Notes
- This game was the first project in a 15-week full-time software engineering bootcamp.

- All logic was written using standard Python — no external game libraries were used.

- The .venv/ folder is excluded from version control using .gitignore.
