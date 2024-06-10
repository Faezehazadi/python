import arcade
from bullet import Bullet
class Spaceship(arcade.Sprite):
    def __init__(self, game_width, game_height):  
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        
        self.center_x = game_width / 2 
        self.center_y = 80
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 50
        self.speed = 10
        self.game_width = game_width
        self.game_height = game_height
        self.bullet_list = []

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed

        elif self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x += self.speed

        elif self.change_y == 1:
            if self.center_y < self.game_height:
                self.center_y += self.speed

        elif self.change_y == -1:
            if self.center_y > 0:
                self.center_y -= self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)