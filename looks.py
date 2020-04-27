import pyxel
from minesweeper import Minesweeper

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
