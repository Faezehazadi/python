import arcade
import arcade.color
from fruit import Flower
from fruit import Leaf
from fruit import Stone
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="  Blak and White Snake 🎮 ")
        arcade.set_background_color(arcade.color.KHAKI)
        self.flower = Flower(self)
        self.leaf = Leaf(self)
        self.stone = Stone(self)
        self.snake = Snake(self)
        self.state = 1

    def on_draw(self):
        arcade.start_render()
        self.flower.draw()
        self.leaf.draw()
        self.stone.draw()
        self.snake.draw()

        arcade.draw_text(f"SCORE: {self.snake.score}", 0.03*self.width, 0.03*self.height, arcade.color.BLACK)

        if self.state == 0: 
            arcade.draw_lrtb_rectangle_filled(0,self.width,self.height,0,arcade.color.BLACK)
            arcade.draw_text("GAME OVER", self.width//6 , self.height//2 , arcade.color.RED, 45)

        arcade.finish_render()

    def on_update(self, delta_time):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.flower):
            del self.flower
            self.snake.score += 2
            self.flower = Flower(self)
        elif arcade.check_for_collision(self.snake, self.leaf):
            del self.leaf
            self.snake.score += 1
            self.leaf = Leaf(self)
        elif arcade.check_for_collision(self.snake, self.stone):
            del self.stone
            self.snake.score -= 1
            self.stone = Stone(self)

            if self.snake.score == 0 or self.snake.score < 0:
                self.state = 0
            
        if self.snake.center_x < 0 or self.snake.center_x > 500 or self.snake.center_y < 0 or self.snake.center_y > self.height:
            self.state = 0

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        

if __name__ == "__main__":
    game = Game()
    arcade.run()
    