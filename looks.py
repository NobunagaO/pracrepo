import pyxel

class App:
    def __init__(self):
        self.display_image = [[True for i in range(10)] for j in range(10)]
        pyxel.init(160, 160, caption="Minesweeper")
        pyxel.load("sample.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.display_image[pyxel.mouse_y // 16][pyxel.mouse_x // 16] = False

    def draw(self):
        pyxel.cls(0)
        #pyxel.blt(0, 0, 0, 0, 0, 16, 16)
        for i in range(10):
            for j in range(10):
                if self.display_image[i][j]:
                    pyxel.blt(16 * j, 16 * i, 0, 0, 0, 16, 16)
        pyxel.text(16, 16, "Hello", pyxel.frame_count % 16)
        self.draw_map()

    def draw_map(self):
        pass

App()
