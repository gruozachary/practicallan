class Path:
    def __init__(self, path: list[tuple[int, int]], word: str):
        self.path = path
        self.word = word

class Solver:
    def __init__(self, word_list: list[str], board: list[list[str]]):
        self.word_list = word_list
        self.board = board
        self.prefix_set = self._create_prefix_set()

    def solve(self) -> list[Path]:
        correct_paths = []
        width = range(len(self.board[0]))
        height = range(len(self.board))
        stack = [[(x, y)] for x in width for y in height]
        while stack:
            top = stack.pop()
            word = self._word(top)
            if not word in self.prefix_set: continue
            if word in self.word_list:
                correct_paths.append(Path(top, word))
            stack.extend([[*top, p] for p in self._neighbours(top)])
        return correct_paths

    def _create_prefix_set(self):
        return { w[:i+1] for w in self.word_list for i in range(len(w)) }

    def _word(self, path: list[tuple[int, int]]):
        return "".join([self.board[y][x] for (x, y) in path])

    def _neighbours(self, path: list[tuple[int, int]]) -> list[tuple[int, int]]:
        (x, y) = path[-1]
        possible = [(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2)]
        correct = filter(lambda p:
            0 <= p[0] < len(self.board[0]) \
            and 0 <= p[1] < len(self.board) \
            and not p in path,
        possible)
        return list(correct)
