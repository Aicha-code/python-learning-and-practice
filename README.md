
# 🐍 Python Learning and Practice

This repository is built as part of my journey to practice **Python programming** exploring data types, logic building, and various programming techniques. Each script focuses on a particular programming exercise from string parsing and formatting, object-oriented programming, and Streamlit apps for web.

Below you'll find a short description, usage examples, and quick run instructions for each Python file in this folder.


## Files in this repository

### `arithmetic-operations-formatter.py`

Purpose
- A CLI app that accepts up to five arithmetic problems and prints them arranged vertically, similar to how problems are formatted on paper. It also optionally displays the answers.

Key behaviors
- Accepts input as a comma-separated list of problems, where each problem is `operand1 operator operand2` (for example: `32 + 698`).
- Validates: at most 5 problems, operands must be digits only, operands up to 4 digits, and operators must be one of `+ - * /`.
- When showing answers, division results are displayed with two decimal places.

Usage (terminal window)
1. Run the script:

```
python .\arithmetic-operations-formatter.py
```

2. Follow the interactive prompts. Example input:

```
Enter the arithmetic problems separated by commas as in the example above: 32 + 698, 3801 - 2, 45 * 43
Do you want to display the answers? (y/n): y
```

Output example

The script will print the arranged problems and (if requested) the answers.


### `polygon-area-calculator.py`

Purpose
- A small object-oriented module with a `Rectangle` class and a `Square` subclass. It uses methods to compute area, perimeter, diagonal, ASCII picture rendering, and how many times another shape fits inside.

Key behaviors
- Rectangle and Square classes with setters that validate inputs (> 0).
- Methods: `get_area()`, `get_perimeter()`, `get_diagonal()`, `get_picture()`, `get_amount_inside(other)`.
- `get_picture()` returns an ASCII-art rectangle unless the shape is larger than 50 in width or height.

Usage (Terminal window / Import)
- You can run it directly:

```
python .\polygon-area-calculator.py
```

- Or import and use the classes from another script or an interactive session:

```python
from polygon_area_calculator import Rectangle, Square

...
```

### `time-calculator.py`

Purpose
- A Streamlit web app and helper function `add_time(start, duration, day_of_week=None)` that adds a duration to a start time and returns the resulting time, optionally including the day of the week and how many days later it is.

Key behaviors
- `add_time` accepts `start` like `3:00 PM`, `duration` like `3:10`, and an optional starting day. It returns a formatted string with the resulting time, day (if provided), and an indicator if the time falls on the next day or multiple days later.
- The top-level `main()` function builds a simple Streamlit UI for interactive use.

Usage (terminal window)
- To run the Streamlit app locally (requires `streamlit` installed):

```
pip install streamlit
streamlit run .\time-calculator.py
```

- Or call access it directly form the web at : 
( https://python-learning-and-practice-7ahb7l8stvfus5rdthezp8.streamlit.app/ )
