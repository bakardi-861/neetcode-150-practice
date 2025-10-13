from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.win = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.win.append(val)
        self.sum += val

        if len(self.win) > self.size:
            self.sum -= self.win.popleft()

        return self.sum / len(self.win)