from random import randint

class Minesweeper():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.realfield = [[0 for j in range(self.width+2)] for i in range(self.height+2)]
        self.outputfield = [[0 for j in range(self.width+2)] for i in range(self.height+2)]
        self.numfield = [[0 for j in range(self.width+2)] for i in range(self.height+2)]

    def set_bombs(self, x, y, cnt):
        cnt = (self.height * self.width - 1) if cnt >= (self.height * self.width - 1) else cnt
        self.realfield[y][x] = 2
        self.outputfield[y][x] = 1
        while True:
            if cnt <= 0:
                break
            x1 = randint(1, self.width)
            y1 = randint(1, self.height)
            if self.realfield[y1][x1] > 0:
                continue
            self.realfield[y1][x1] = 1
            cnt -= 1
        for i in range(1, self.height+1):
            for j in range(1, self.width+1):
                self.numfield[i][j] = self.count_around(j, i)

    def count_around(self, x, y):
        cnt = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.realfield[y+i][x+j] == 1:
                    cnt += 1
        return cnt

    def print_field(self, field):
        for i in range(1, self.height+1):
            for j in range(1, self.width+1):
                print(field[i][j], end=",")
            print()

if __name__ == "__main__":
    m = Minesweeper(10, 10)
    m.set_bombs(1, 1, 10)
    m.print_field(m.realfield)
    m.print_field(m.numfield)
