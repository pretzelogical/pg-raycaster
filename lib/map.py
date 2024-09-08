

class Map:
    def __init__(self):
        self.width = 8
        self.height = 8
        # self.data = [0] * (width * height)
        self.data = [
          [1] * self.width,
          [1, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 1, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1] * self.width,
        ]

    def get_tile(self, x: int, y: int):
        return self.data[y][x]
