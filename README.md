# Python Projects Collection

This repository hosts a collection of Python projects including mini-games and utility applications. Each project is designed to be simple, fun, and serves as a great example for basic Python concepts and game development.

## Projects Included

Currently, this repository includes the following projects:

### Games

*   **Pong Game** (`pong-game/`): A classic two-player arcade game where players control paddles to hit a ball back and forth.
*   **Snake Game** (`snake_game/`): The timeless arcade game where the player controls a growing snake, trying to eat food while avoiding collisions with walls or its own body.
*   **Turtle Crossing** (`turtle-crossing/`): A game where the player controls a turtle attempting to cross a busy road without being hit by cars.
*   **U.S. States Game** (`us_states_game/`): An educational game where players guess U.S. states and learn their locations on a map.

### Utilities

*   **Miles to Kilometer Converter** (`mile_to_kilo_convert/`): A simple GUI application built with Tkinter that converts miles to kilometers.
*   **NATO Phonetic Alphabet** (`NATO-alphabet-start/`): A utility that converts words into NATO phonetic alphabet codes using a CSV dataset.
*   **Quizzler App** (`quizzler-app-start/`): A GUI trivia quiz app that presents true/false questions, tracks the score, and displays feedback after each answer using Tkinter.

## Technologies Used

*   **Python**: The primary programming language for all projects.
*   **Libraries**: 
    - `turtle`: Used for graphics in games and the U.S. States game
    - `tkinter`: Used for the GUI converter application
    - `pandas`: Used for data handling in the NATO alphabet and U.S. States game
*   **Docker**: The repository includes a `Dockerfile` for running any project inside a container.

## Running with Docker

A `Dockerfile` is included to run any project inside a container without needing a local Python installation. By default it runs the Snake Game, but you can override the target project using environment variables.

1. **Build the image**:
    ```bash
    docker build -t python-projects .
    ```
2. **Run the default project** (Snake Game):
    ```bash
    docker run -e DISPLAY=$DISPLAY python-projects
    ```
3. **Run a different project** by setting `GAME_DIR` and `GAME_FILE`:
    ```bash
    docker run -e GAME_DIR=quizzler-app-start -e GAME_FILE=main.py python-projects
    ```

> **Note**: GUI-based projects (turtle, Tkinter) require a display server (e.g., X11 on Linux/WSL or XQuartz on macOS) to be forwarded into the container.

## How to Run the Games

To run any of these games, you will need Python installed on your system.

1.  **Clone the Repository**:
    First, clone this repository to your local machine using Git:
    ```bash
    git clone https://github.com/roy3177/Mini-games.git
    ```
2.  **Navigate to a Game Directory**:
    Change into the directory of the game you wish to play. For example, to play the Snake Game:
    ```bash
    cd Mini-games/snake_game
    ```
3.  **Run the Game**:
    Execute the main Python script for the game. The exact script name might vary, but it's typically `main.py` or `[game_name].py`.
    ```bash
    python [game_script_name].py
    ```
    (e.g., `python snake_game.py` or `python main.py` if a `main.py` exists in the game folder)

    Repeat this process for other games by navigating to their respective directories.

## Folder Structure

The repository is organized with each game residing in its own dedicated folder:

```
PycharmProjects/
│
├── pong-game/
├── snake_game/
├── turtle-crossing/
├── us_states_game/
├── mile_to_kilo_convert/
├── NATO-alphabet-start/
├── quizzler-app-start/
├── Dockerfile
├── .gitignore
└── README.md
```


## Contributing

If you have suggestions for improvements, bug fixes, or new mini-games to add, feel free to fork the repository, make your changes, and submit a pull request.

## Author

*   **roy3177** - [GitHub Profile](https://github.com/roy3177)
