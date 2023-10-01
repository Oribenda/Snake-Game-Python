# Snake-Game-Python

![Snake Game](gameplay.gif)

## Introduction

Welcome to my Snake Game project! This classic Snake game is implemented in Python using the Pygame library.

## Getting Started

To play the Snake Game, follow these simple steps:

1. **Clone or Download**: You can clone this repository to your local machine using Git or download it as a ZIP file.

2. **Prerequisites**: Ensure that you have Python and Pygame installed on your system. If not, you can install Python from the [official Python website](https://www.python.org/downloads/), and Pygame can be installed via pip:

   ```shell
   pip install pygame
   ```

3. **Run the Game**: Execute the game by running the `snake_game.py` script:

   ```shell
   python snake.py
   ```

4. **Game Controls**:
   - Use the arrow keys (Up, Down, Left, Right) to control the snake's direction.
   - Press the "Exit" key (Q) to quit the game.

## Gameplay

- Your snake starts with a length of 6 segments and appears on the screen.
- Control the snake to eat red squares, representing food, to grow longer and increase your score.
- The game ends if the snake collides with the screen boundaries or itself.

## Game Features

- Real-time scoring displayed in the top-left corner.
- Smooth controls and movement for an enjoyable gaming experience.
- Randomized food placement for added challenge.

## Customization

Feel free to customize various aspects of the game:

- **Window Size**: Adjust the game window size by modifying the `WINDOW_HEIGHT` and `WINDOW_WIDTH` constants in the code.

- **Speed**: Modify the snake's speed by adjusting the `clock.tick` value in the `play_game` function.

- **Colors**: Customize the game's appearance by updating color constants in the `colours` module.

- **Initial Snake Length**: Change the initial snake length by modifying the `snake_positions` list in the `play_game` function.
