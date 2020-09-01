import arcade
from beater import Beater
from falling import Falling
from score import Score
from record import Record


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.__WIDTH = width
        self.__HEIGHT = height
        self.__TITLE = title
        self.bg_texture = arcade.load_texture('images/background.png')

        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.beater = Beater(self.__WIDTH * .5, self.__HEIGHT * .02,
                             self.__WIDTH, self.__HEIGHT)
        self.__falling_speed = 3
        self.falling_list = [Falling(self.__WIDTH, self.__HEIGHT,
                                     speed=self.__falling_speed)]
        self.score = Score()

        self.pause = True
        self.mouse_use = False
        self.lose = False

        self.record = Record(self.score.score)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.__WIDTH / 2, self.__HEIGHT / 2,
                                      self.__WIDTH, self.__HEIGHT,
                                      self.bg_texture, 0)
        if not self.lose:
            self.beater.draw()
            for falling in self.falling_list:
                falling.draw()
            if self.pause:
                arcade.draw_text("Options: ",
                                 10, self.__HEIGHT * .9,
                                 arcade.color.BLACK, 20)
                arcade.draw_text("1. Additional falling (20)",
                                 10, self.__HEIGHT * .8,
                                 arcade.color.BLACK, 20)
                arcade.draw_text("2. Slow (40)",
                                 10, self.__HEIGHT * .7,
                                 arcade.color.BLACK, 20)
                arcade.draw_text("3. Mouse using (100)",
                                 10, self.__HEIGHT * .6,
                                 arcade.color.BLACK, 20)
                arcade.draw_text("Press \"P\" to start",
                                 self.__WIDTH / 3, self.__HEIGHT / 2,
                                 arcade.color.BLACK, 40)
            else:
                arcade.draw_text(str(self.score.score),
                                 self.__WIDTH / 2 * .95, self.__HEIGHT / 2,
                                 arcade.color.BLACK, 60)
        else:
            best = self.record.best()
            arcade.draw_text("Score: " + str(self.score.score),
                             self.__WIDTH / 2, self.__HEIGHT * .8,
                             arcade.color.BLACK, 40)
            arcade.draw_text("Records:",
                             self.__WIDTH / 3, self.__HEIGHT * .7,
                             arcade.color.BLACK, 40)
            arcade.draw_text(best[0][1] + " " + str(best[0][0]),
                             self.__WIDTH / 2.5, self.__HEIGHT * .6,
                             arcade.color.BLACK, 40)
            arcade.draw_text(best[1][1] + " " + str(best[1][0]),
                             self.__WIDTH / 2.5, self.__HEIGHT * .5,
                             arcade.color.BLACK, 40)
            arcade.draw_text(best[2][1] + " " + str(best[2][0]),
                             self.__WIDTH / 2.5, self.__HEIGHT * .4,
                             arcade.color.BLACK, 40)

    def on_update(self, delta_time):
        if not self.pause and not self.lose:
            self.beater.update()
            for falling in self.falling_list:
                falling.update()
            self.__falling_catch()

    def on_key_press(self, key, modifiers):
        if not self.lose:
            if key == arcade.key.RIGHT:
                self.beater.x_change = self.beater.speed
            if key == arcade.key.LEFT:
                self.beater.x_change = -self.beater.speed
            if key == arcade.key.P:
                if self.pause:
                    self.pause = False
                else:
                    self.pause = True

            if key == arcade.key.KEY_1 and self.score.score >= 20:
                self.__append_falling(self.__falling_speed)
                self.score.increase(-20)
            if key == arcade.key.KEY_2 and self.score.score >= 40:
                self.__falling_speed = 3
                self.score.increase(-40)
            if key == arcade.key.KEY_3 and self.score.score >= 100 and not self.mouse_use:
                self.mouse_use = True
                self.score.increase(-100)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.beater.x_change = 0
        if key == arcade.key.LEFT:
            self.beater.x_change = 0

    def on_mouse_motion(self, x, y, dx, dy):
        if self.mouse_use:
            self.beater.x_pos = x

    def __falling_catch(self):
        for falling in self.falling_list:
            if self.beater.x_pos - self.beater.width / 2 <= falling.x_pos <= \
                    self.beater.x_pos + self.beater.width / 2 and \
                    self.beater.y_pos - self.beater.height / 2 <= falling.y_pos <= \
                    self.beater.y_pos + self.beater.height / 2:
                falling.speed = 0
                self.falling_list.remove(falling)
                del falling
                self.__append_falling(self.__falling_speed)

                self.__point_up(10, 20)
                self.__point_up(70, 40)
                self.__point_up(150, 80)
                self.__point_up(300, 150)
                self.__point_up(500, 275)
                self.__point_up(950, 400)
                self.__point_up(1500, 750)

                self.score.increase()
                increase = 0.2
                self.__falling_speed += increase
                self.beater.speed += increase
            elif falling.y_pos < 0:
                self.falling_list.remove(falling)
                del falling
                self.__falling_speed += 5
                self.score.score -= 20
                if len(self.falling_list) == 0:
                    self.score.score += 20
                    self.record.count = self.score.score
                    self.record.enter()
                    self.lose = True

    def __append_falling(self, speed):
        self.falling_list.append(Falling(self.__WIDTH, self.__HEIGHT,
                                         speed=speed))

    def __point_up(self, score, additional):
        if self.score.score == score:
            self.__append_falling(3)
            self.__falling_speed = 3
            self.score.score += additional

    def run(self):
        arcade.run()
