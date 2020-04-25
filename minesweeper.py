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
                if self.realfield[i][j] == 1:
                    self.numfield[i][j] = 9

    def count_around(self, x, y):
        cnt = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.realfield[y+i][x+j] == 1:
                    cnt += 1
        return cnt

    def open_here(self, x, y):
        self.outputfield[y][x] = 1

    def print_field(self, field):
        for i in range(1, self.height+1):
            for j in range(1, self.width+1):
                print(field[i][j], end=",")
            print()

    def play_game(self, cnt):
        x, y = [int(i) for i in input().split()]
        self.set_bombs(x, y, cnt)
        self.output_field()
        while True:
            print("="*10)
            x, y = [int(i) for i in input().split()]
            self.open_here(x, y)
            self.output_field()
            if self.numfield[y][x] == 9:
                break

    def output_field(self):
        for i in range(1, self.height+1):
            for j in range(1, self.width+1):
                out = str(self.numfield[i][j]) if self.outputfield[i][j] == 1 \
                        and self.numfield[i][j] != 9 \
                        else "B" if self.outputfield[i][j] == 1 and self.numfield[i][j] == 9 \
                        else "#"
                print(out,end="")
            print()

if __name__ == "__main__":
    m = Minesweeper(10, 10)
    m.play_game(10)
