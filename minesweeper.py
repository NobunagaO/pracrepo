from random import randint

class Minesweeper:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.realfield = [[0 for j in range(self.width+2)] for i in range(self.height+2)]
        self.outputfield = [[0 for j in range(self.width+2)] for i in range(self.height+2)]
        self.numfield = [[0 for j in range(self.width+2)] for i in range(self.height+2)]

    def set_bombs(self, x, y, cnt):
        cnt = (self.height * self.width - 1) if cnt >= (self.height * self.width - 1) else cnt
        self.realfield[y][x] = 2
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
        self.open_function(x, y)

    def count_around(self, x, y):
        cnt = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.realfield[y+i][x+j] == 1:
                    cnt += 1
        return cnt

    def open_function(self, x, y):
        if self.numfield[y][x] == 0 and self.outputfield[y][x] != 1:
            self.outputfield[y][x] = 1
            self.open_around(x, y)
        else:
            self.outputfield[y][x] = 1

    def open_around(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.numfield[y+i][x+j] != 0:
                    self.outputfield[y+i][x+j] = 1
                if x+j > 0 and x+j < self.width+1 and y+i > 0 and y+i < self.height+1:
                    self.open_function(x+j, y+i)

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
            self.open_function(x, y)
            self.output_field()
            if self.numfield[y][x] == 9:
                break

    def output_field(self):
        for i in range(1, self.height+1):
            for j in range(1, self.width+1):
                out = str(self.numfield[i][j]) if self.outputfield[i][j] == 1 \
                        and self.numfield[i][j] != 9 \
                        else "B" if self.outputfield[i][j] == 1 \
                        and self.numfield[i][j] == 9 else "#"
                print(out,end="")
            print()

import pyxel

class App:
    def __init__(self):
        self.mine = Minesweeper(10, 10)
        self.count = 0
        self.game_clear = False
        self.game_over = False
        pyxel.init(160, 160, caption="Pyxel Minesweeper")
        pyxel.load("assets/sample.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            x = pyxel.mouse_x // 16 + 1
            y = pyxel.mouse_y // 16 + 1
            if self.count == 0:
                self.mine.set_bombs(x, y, 10)
            else:
                self.mine.open_function(x, y)
                self.clear_game()
                if self.mine.numfield[y][x] == 9:
                    self.game_over = True
            self.count += 1
            # self.display_image[pyxel.mouse_y // 16][pyxel.mouse_x // 16] = False

    def draw(self):
        pyxel.cls(0)
        # pyxel.blt(0, 0, 0, 0, 0, 16, 16)
        # if self.game_over:
            # pyxel.text(40, 75, "Game Over", pyxel.frame_count % 16)
        for i in range(1, 12):
            for j in range(1, 12):
                pass
                # if self.display_image[i][j]:
                if self.mine.outputfield[i][j] == 0:
                    pyxel.blt(16 * (j-1), 16 * (i-1), 0, 0, 0, 16, 16)
                elif self.mine.numfield[i][j] not in  [0, 9]:
                    pyxel.blt(16 * (j-1), 16 * (i-1), 0, 16 * (self.mine.numfield[i][j] + 1), 0 , 16, 16)
                elif self.mine.numfield[i][j] == 0:
                    pyxel.blt(16 * (j-1), 16 * (i-1), 0, 16 * 10 , 0, 16, 16)
                else:
                    pyxel.blt(16 * (j-1), 16 * (i-1), 0, 16, 0, 16, 16)
        # pyxel.text(16, 16, "Hello", pyxel.frame_count % 16)
        if self.game_over:
            pyxel.text(40, 75, "Game Over", pyxel.frame_count % 16)
        if self.game_clear:
            pyxel.text(40, 75, "Game Clear", pyxel.frame_count % 16)
    def clear_game(self):
        count = 0
        for i in range(1, 12):
            count += self.mine.outputfield[i].count(1)
        if count == 90:
            self.game_clear = True


App()
