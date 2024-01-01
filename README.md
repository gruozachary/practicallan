# practicallan

## About
**practicallan** is the algorithm used in [anticallan](https://github.com/gruozachary/anticallan), ported to python and packaged as a library.

It provides functionality to find all of the valid words that can be traced in a grid of characters, e.g., the "WordHunt" game in [GamePigeon](https://gamepigeonapp.com/).

## Usage
Simply install the package from git using pip (I recommend using a virtual environment, such as [venv](https://docs.python.org/3/library/venv.html)):
```
pip install git+https://github.com/gruozachary/practicallan.git
```
Then you can use it in your code. Here is an example:
```python
import practicallan

# Initialise word list and board to be used

word_list = open("<path_to_word_list>").read().split('\n')
board = [["R", "S", "P", "E"],
         ["H", "Y", "P", "N"],
         ["A", "U", "T", "O"],
         ["Y", "E", "R", "O"]]

# Use the `solve` function to produce the words and paths from the word list and board

x = practicallan.solve(word_list, board)

# Sort the resultant list so the longest words are visible at the bottom of the terminal

x.sort(key=lambda x: len(x.word))

for word_path in x:
    print(word_path.word)
```
