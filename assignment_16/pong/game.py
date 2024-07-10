import arcade
from ball import Ball
from rocket import Rocket

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=700 ,title="Pong 🏆")
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)
        self.player1=Rocket(40,self.height//2, arcade.color.MAGENTA,"Faezeh")
        self.player2=Rocket(self.width-40, self.height//2,arcade.color.ROSE_MADDER,"Computer")
        self.ball=Ball(self)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_outline(self.width//2,self.height//2, self.width-10,self.height-10,arcade.color.WHITE,border_width=30)
        arcade.draw_line(self.width//2,30,self.width//2,self.height-30, arcade.color.WHITE,line_width=10)
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
        arcade.draw_text(f"{self.player1.score}"+71*" "+f"{self.player2.score}", 50,50,arcade.color.WHITE, 30)
   
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player1.height<y<self.height-self.player1.height:
            self.player1.center_y = y

    def on_update(self, delta_time: float):

        self.player2.move(self.ball,self)  
        
        if self.ball.center_y <30 or self.ball.center_y>self.height-30:
            self.ball.change_y *= -1
        if arcade.check_for_collision(self.ball,self.player1) or\
        arcade.check_for_collision(self.ball,self.player2):
            self.ball.change_x *= -1

        if self.ball.center_x<self.player1.center_x:
            print("🎈")
            self.player2.score+=1
            del self.ball
            self.ball=Ball(self)
        if self.ball.center_x>self.player2.center_x:
            print("🎈")
            self.player1.score+=1
            del self.ball
            self.ball=Ball(self)

        self.ball.move()
        