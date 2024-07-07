import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 30
        self.height = 30
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.BLACK
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.body = []
        self.bodyyList = arcade.SpriteList()
         

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

        for i in range(len(self.body)):
            if i%2==0:
                arcade.draw_rectangle_filled(self.body[i]['x'],self.body[i]['y'],self.width,self.height,self.color)
            else:
                arcade.draw_rectangle_filled(self.body[i]['x'],self.body[i]['y'],self.width,self.height,arcade.color.WHITE)

    def move(self):

        self.body.append({'x':self.center_x, 'y':self.center_y})  
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        