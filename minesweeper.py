from random import randint

class Minesweeper():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.realfield = [[0 for j in range(self.width)] for i in range(self.height)]
        self.outputfield = [[0 for j in range(self.width)] for i in range(self.height)]
        self.numfield = [[0 for j in range(self.width)] for i in range(self.height)]

    def set_bombs(self, x, y, cnt):
        cnt = (self.height * self.width - 1) if cnt >= (self.height * self.width - 1) else cnt
        self.realfield[y][x] = 2
        self.outputfield[y][x] = 1
        while True:
            if cnt <= 0:
                break
            x1 = randint(0, self.width)
            y1 = randint(0, self.height)
            if self.realfield[y1][x1] > 0:
                continue
            self.realfield[y1][x1] = 1
            cnt -= 1

    def print_field(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.realfield[i][j], end=",")
            print()

if __name__ == "__main__":
    m = Minesweeper(10, 10)
    m.set_bombs(1, 1, 10)
    m.print_field()
