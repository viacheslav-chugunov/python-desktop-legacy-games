import arcade
import ball
import player
import game_events


class GameWindow(arcade.Window):

    def __init__(self, width, height, title='Ping-Pong'):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        super().__init__(width, height, title)
        self.set_location(100, 50)

        self.background_texture = arcade.load_texture('image/table.png')

        self.SCALE_X = self.SCREEN_WIDTH / self.background_texture.width
        self.SCALE_Y = self.SCREEN_HEIGHT / self.background_texture.height
        self.SPRITE_SCALE = min(self.SCALE_X, self.SCALE_Y) / 5

        self.p1 = player.Player(8 * self.SCALE_X,
                                self.SCREEN_HEIGHT // 2,
                                self.SPRITE_SCALE, 10, 'image/p1.png')

        self.p2 = player.Player(self.SCREEN_WIDTH - 8 * self.SCALE_X,
                                self.SCREEN_HEIGHT // 2,
                                self.SPRITE_SCALE, 10, 'image/p2.png')

        self.ball = ball.Ball(self.SCREEN_WIDTH // 2,
                              self.SCREEN_HEIGHT // 2,
                              self.SPRITE_SCALE * 2, 5)

        # group all sprites to list
        self.sprite_list = arcade.SpriteList()

        self.sprite_list.append(self.p1.sprite)
        self.sprite_list.append(self.p2.sprite)
        self.sprite_list.append(self.ball.sprite)

        # events
        self.events = game_events.GameEvents()

        # beats nums
        self.beats = 0

    def on_draw(self):
        arcade.start_render()

        # setup background texture
        central_pos_x = self.SCREEN_WIDTH // 2
        central_pos_y = self.SCREEN_HEIGHT // 2
        arcade.draw_texture_rectangle(central_pos_x, central_pos_y,
                                      self.background_texture.width * self.SCALE_X,
                                      self.background_texture.height * self.SCALE_Y,
                                      self.background_texture, 0)

        self.sprite_list.draw()

    def on_update(self, delta_time):
        if self.events.IS_STARTED and not self.events.IS_ENDED:

            # p1 updating
            if not self.events.P1_BOT:
                self._player_updating_pos(self.p1)
            else:
                self._ai_logic(self.p1)

            # p2 updating
            if not self.events.P2_BOT:
                self._player_updating_pos(self.p2)
            else:
                self._ai_logic(self.p2)

            # ball updating
            self._ball_moving_logic()

    def on_key_press(self, symbol, modifiers):
        # p1 controller
        if symbol == arcade.key.W:
            self.p1.change_y = self.p1.speed
        if symbol == arcade.key.S:
            self.p1.change_y = -self.p1.speed

        # p2 controller
        if symbol == arcade.key.UP:
            self.p2.change_y = self.p2.speed
        if symbol == arcade.key.DOWN:
            self.p2.change_y = -self.p2.speed

        # switch on/off bot
        if symbol == arcade.key.KEY_1:
            self.events.P1_BOT = True if not self.events.P1_BOT else False
        if symbol == arcade.key.KEY_2:
            self.events.P2_BOT = True if not self.events.P2_BOT else False

        # switch on/off pause
        if symbol == arcade.key.P:
            self.events.IS_STARTED = True if not self.events.IS_STARTED else False

    def on_key_release(self, symbol, modifiers):
        # p1 controller
        if symbol == arcade.key.W:
            self.p1.change_y = 0
        if symbol == arcade.key.S:
            self.p1.change_y = 0

        # p2 controller
        if symbol == arcade.key.UP:
            self.p2.change_y = 0
        if symbol == arcade.key.DOWN:
            self.p2.change_y = 0

    def _ball_moving_logic(self, speed_up=0.4):
        ball_y_up = self.ball.y + self.ball.change_y + self.ball.sprite.width
        ball_y_down = self.ball.y + self.ball.change_y - self.ball.sprite.width
        ball_x_right = self.ball.x + self.ball.change_x + self.ball.sprite.width
        ball_x_left = self.ball.x + self.ball.change_x - self.ball.sprite.width
        delta = 5 * max(self.SCALE_X, self.SCALE_Y)

        self.ball.x += self.ball.change_x

        p2_lover = self.p2.sprite.bottom - delta
        p2_upper = self.p2.sprite.top + delta
        p2_right = self.p2.sprite.right - delta
        p1_lover = self.p1.sprite.bottom - delta
        p1_upper = self.p1.sprite.top + delta
        p1_left = self.p1.sprite.left + delta

        if (p2_lover <= ball_y_up <= p2_upper and p2_right <= ball_x_right <= p2_right + delta) \
                or (p1_lover <= ball_y_down <= p1_upper and p1_left - delta <= ball_x_left <= p1_left):

            self.ball.change_x = -self.ball.change_x

            if self.ball.change_x > 0:
                self.ball.change_x += speed_up
            else:
                self.ball.change_x -= speed_up

            if self.ball.change_y > 0:
                self.ball.change_y += speed_up
            else:
                self.ball.change_y -= speed_up

        elif ball_x_right >= self.SCREEN_WIDTH + 20 * self.SCALE_X or ball_x_left <= -20 * self.SCALE_X:
            self.ball.change_x = self.ball.change_y = 0
            self.IS_ENDED = True

        if ball_y_up < self.SCREEN_HEIGHT and ball_y_down > 0:
            self.ball.y += self.ball.change_y
        else:
            self.ball.change_y = -self.ball.change_y

        self.ball.sprite.set_position(self.ball.x, self.ball.y)

    def _player_updating_pos(self, p):
        upper = p.y + p.change_y + p.sprite.height / 2
        lower = p.y + p.change_y - p.sprite.height / 2
        if upper < self.SCREEN_HEIGHT and lower > 0:
            p.y += p.change_y
            p.sprite.set_position(p.x, p.y)

    def _ai_logic(self, p):
        p.y = self.ball.y
        p.sprite.set_position(p.x, p.y)


if __name__ == '__main__':
    GameWindow(1280, 720)
    arcade.run()
