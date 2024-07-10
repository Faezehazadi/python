import arcade
from rocket import Rocket
from brick import Brick
from heart import Heart
from ball import Ball

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=600, title= " Breakout 🧱")
        arcade.set_background_color(arcade.color.DARK_OLIVE_GREEN)
        #obj
        self.rocket = Rocket(self)
        self.ball = Ball(self)
        #list
        self.brick_list = []
        #color for bricks
        self.color_list = [arcade.color.ARSENIC, arcade.color.ANTIQUE_FUCHSIA, arcade.color.BAKER_MILLER_PINK, arcade.color.AQUAMARINE, arcade.color.ATOMIC_TANGERINE, arcade.color.BABY_POWDER]
        self.heart_list = []

        #make bricks
        for row in range(6):
            for col in range(10):
                brick = Brick (row, col, self.color_list[row])
                brick.center_x = 25 + col * 50
                brick.center_y = 500 - row * 25
                self.brick_list.append(brick)

        #make hearts
        for h in range(1, 4):
            self.heart = Heart(h+1)
            self.heart_list.append(self.heart)

    #draw obj
    def on_draw(self):
        arcade.start_render()

        self.rocket.draw()

        self.ball.draw()
        
        for brick in self.brick_list:
            brick.draw()

        for heart in self.heart_list:
            heart.draw()    
  
        arcade.draw_text(f"SCORE: {self.rocket.score}", 20, 550,arcade.color.WHITE,20, font_name=("segoe print") ,bold= True)

        #Gameover    
        if len(self.heart_list) == 0:
             arcade.draw_lrtb_rectangle_filled(0, 500, 600, 0, arcade.color.ANTIQUE_RUBY)
             arcade.draw_text("GAME OVER", 100,300, arcade.color.WHITE, 40)   
             del self.ball
             del self.rocket 
         #Win    
        if len(self.brick_list)==0:
          arcade.draw_text(" Congrate",100, 300, arcade.color.WHITE, 40) 
          del self.ball
          del self.rocket      

        arcade.finish_render()

    #mouse_motion
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.rocket.height < y < self.height-self.rocket.height:
           self.rocket.center_x = x
        # self.rocket.center_y = y

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.rocket.chenge_x = 1

        if symbol == arcade.key.LEFT:
            self.rocket.change_x = -1


    def on_update(self, delta_time):
        self.ball.move()
        
        #collision ball and brick
        for brick in self.brick_list:
            if arcade.check_for_collision(self.ball, brick):
                self.brick_list.remove(brick)
                self.ball.change_y *=-1
                self.rocket.score +=1
                
        #collision ball and wall
        if self.ball.center_x < 0 or self.ball.center_x > self.width:
            self.ball.change_x *=-1

        #collision ball and height
        if self.ball.center_y > self.height:
            self.ball.change_y= -1

        #collision ball and rocket
        if arcade.check_for_collision(self.ball, self.rocket):
            self.ball.change_y = 1

        #if the ball goes out of the buttom of the screen (score --)
        if self.ball.center_y <0:
            if len(self.heart_list) >0:
                self.heart_list.pop(-1)
                del self.ball
                self.ball = Ball(self)

game = Game()
arcade.run()