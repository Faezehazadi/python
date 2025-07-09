import random
import arcade
import arcade.key
import arcade.key
from spaceship import Spaceship
from enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=600, title="Spaceship 🚀")
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.background = arcade.load_texture("pic/galaxy.png")
        self.me = Spaceship(self.width, self.height)
        self.enemies = []
        self.speed_increase = 0.1
        self.elapsed_time = 0
        self.heal = 3
        self.score = 0
        self.game_over = False

    def on_draw(self):
        arcade.start_render()
        if not self.game_over:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
            self.me.draw()
            for enemy in self.enemies:
                enemy.draw()
            for bullet in self.me.bullet_list:
                bullet.draw()
        else:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("GAME OVER", self.width // 2, self.height // 2, arcade.color.RED, 32,
                            align="center", anchor_x="center", anchor_y="center", width=self.width)
        health_display = " ".join(["◼" for _ in range(self.heal)])
        arcade.draw_text(f"Score: {self.score}", 20, 15, arcade.color.WHITE, 14)
        arcade.draw_text(f"Hearts: {health_display}", self.width - 200, 15, arcade.color.WHITE, 14)
        

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.me.change_x = 1

        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.me.change_x = -1            

        elif symbol == arcade.key.UP or symbol == arcade.key.W:
            self.me.change_y = 1

        elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.me.change_y = -1

        elif symbol == arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0
        self.me.change_y = 0

    def on_update(self, delta_time: float):
        if not self.game_over:
            self.elapsed_time += delta_time
            if self.elapsed_time > 3:
                new_enemy = Enemy(self.width, self.height, initial_speed=1.5 + self.speed_increase)
                self.enemies.append(new_enemy)
                self.elapsed_time = 0
                self.speed_increase += 0.05

            for enemy in self.enemies:
                if arcade.check_for_collision(self.me, enemy):
                    self.heal -= 1
                    self.enemies.remove(enemy)
                    if self.heal <= 0:
                        self.game_over = True
                        return
                if enemy.center_y < 0:
                    self.heal -= 1
                    self.enemies.remove(enemy)
                    if self.heal <= 0:
                        self.game_over = True
                        return

            for enemy in self.enemies:
                for bullet in self.me.bullet_list:
                    if arcade.check_for_collision(bullet, enemy):
                        self.enemies.remove(enemy)
                        self.me.bullet_list.remove(bullet)
                        self.score += 1
                        
            self.me.move()

            for bullet in self.me.bullet_list:
                bullet.move()

            for enemy in self.enemies:
                if enemy.center_y < 0:
                    self.enemies.remove(enemy)
            
            for bullet in self.me.bullet_list:
                if bullet.center_y > self.height:
                    self.me.bullet_list.remove(bullet)

            for enemy in self.enemies:
                enemy.move()
            if random.randint(1, 150) == 10:
                self.new_enemy = Enemy(self.width, self.height)
                self.enemies.append(self.new_enemy)

        else:
            arcade.set_background_color(arcade.color.BLACK)

window = Game()
arcade.run()