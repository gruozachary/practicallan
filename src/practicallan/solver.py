class Path:
    def __init__(self, path: list[tuple[int, int]], word: str):
        self.path = path
        self.word = word

class Solver:
    def __init__(self, word_list: list[str], board: list[list[str]]):
        self.word_list = word_list
        self.board = board

    def solve(self) -> list[Path]:
        correct_paths = []
        width = range(len(self.board[0]))
        height = range(len(self.board))
        stack = [[(x, y)] for x in width for y in height]
        while stack:
            top = stack.pop()
            word = self._word(top)
            real = False
            for real_word in self.word_list:
                if real_word.startswith(word):
                    real = True
                    break
            if not real: continue
            if word in self.word_list:
                correct_paths.append(Path(top, word))
            stack.extend([[*top, p] for p in self._neighbours(top)])
        return correct_paths


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
