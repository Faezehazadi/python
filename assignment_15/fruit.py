import random
import arcade

class Fruit(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 50
        self.height = 50
        self.center_x = random.randint(20, 500-20)
        self.center_y = random.randint(20, 500-20)
        self.change_x = 0
        self.change_y = 0

class Flower(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.pic=arcade.load_texture("pic/flower.png")

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)

class Leaf(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.pic=arcade.load_texture("pic/leaf.png")

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)

class Stone(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.pic=arcade.load_texture("pic/stone.png")

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)
        