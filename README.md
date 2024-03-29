# Pomodoro Timer

This is a simple Pomodoro timer application built using Python's tkinter library. The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Features

- Allows users to set work intervals, short break intervals, and long break intervals.
- Displays a countdown timer for each interval.
- Notifies users with different colors and text labels for work intervals, short breaks, and long breaks.
- Keeps track of completed work sessions with checkmarks.

## Usage

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the `main.py` file.
4. The application window will open, allowing you to start the timer, reset the timer, and view the progress with checkmarks.

## Dependencies

- Python 3.x
- tkinter library

## How It Works

The application uses tkinter for the graphical user interface. It defines constants for colors, font, and interval lengths. The `start_timer()` function manages the timer mechanism, including starting the timer for work intervals, short breaks, and long breaks. The `count_down()` function handles the countdown mechanism, updating the timer display and managing the progression of intervals. The application also provides functionality to reset the timer.


