# TypinBot

This Python script provides a bot for automating typing tests on various typing websites using the Selenium framework. The bot can type on multiple typing websites, each implemented as a separate function within the `TestTyping` class. The functions are accessible through the CLI given by `run.py`. Most other websites (that don't use HTML canvas to print text) can be automated using the `Chrome` and `CustomTyper` classes.

## Dependencies

- `selenium`: A Python library for automating web browsers.

## Usage

1.  Install Chrome and Python if not already installed. 
2.  Install the required dependencies:
  ```bash
   pip install selenium
  ```
3. Run the program:
   ```bash
   python run.py
   ```
