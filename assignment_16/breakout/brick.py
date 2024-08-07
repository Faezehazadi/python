import arcade

class Brick(arcade.Sprite):
    def __init__(self, x, y, c):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.change_x = 0
        self.change = 0
        self.width = 39
        self.height = 15


    def draw(self):
        arcade.draw_rectangle_outline(self.center_x, self.center_y, self.width, self.height, self.color, border_width= 5 )