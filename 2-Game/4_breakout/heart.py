import arcade

class Heart(arcade.Sprite):
    def __init__(self, x):
        super().__init__("breakout\pic\heart.png")
        self.center_x = 30*x
        self.center_y = 28
        self.width = 30
        self.height = 30