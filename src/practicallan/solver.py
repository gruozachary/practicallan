"""Contains logic and helper struct for solving the game"""

from dataclasses import dataclass

@dataclass
class WordPath:
    """Struct containing data about a path around a board"""

    word: str
    cartesian_path: list[tuple[int, int]]

def _prefix_set(word_list: list[str]) -> set[str]:
    return { w[:i+1] for w in word_list for i in range(len(w)) }

def _path_to_word(board: list[list[str]], path: list[tuple[int, int]]) -> str:
    return "".join([board[y][x] for (x, y) in path])

def _neighbours(board: list[list[str]], path: list[tuple[int, int]]) -> list[tuple[int, int]]:
    (pos_x, pos_y) = path[-1]
    possible = [(i, j) for i in range(pos_x-1, pos_x+2) for j in range(pos_y-1, pos_y+2)]
    correct = filter(lambda p:
        0 <= p[0] < len(board[0]) \
        and 0 <= p[1] < len(board) \
        and not p in path,
    possible)
    return list(correct)

def solve(word_list: list[str], board: list[list[str]]) -> list[WordPath]:
    """Given word_list and board, solves the game"""

    prefix_set = _prefix_set(word_list)
    correct_paths = []
    width = range(len(board[0]))
    height = range(len(board))
    stack = [[(x, y)] for x in width for y in height]
    while stack:
        top = stack.pop()
        word = _path_to_word(board, top)
        if not word in prefix_set:
            continue
        if word in word_list:
            correct_paths.append(WordPath(word, top))
        stack.extend([[*top, p] for p in _neighbours(board, top)])
    return correct_paths
