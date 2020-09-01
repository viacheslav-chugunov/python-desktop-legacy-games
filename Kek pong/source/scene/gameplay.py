import arcade
from ..config import RESOLUTION
from ..scene.scene import Scene
from ..sprite.beater import Beater
from ..sprite.ball import Ball
from ..sprite.goal import Goal
from ..sprite.heal import Heal
from time import time
from random import randrange


class Gameplay(Scene):
    def __init__(self, parent, max_score=5, ai=True):
        super().__init__(arcade.load_texture('media/images/scene/gameplay/bg.png'), parent)
        self._player1 = Beater(RESOLUTION[0] * .05, RESOLUTION[1] * .5, keyboard=True,
                               keys=(arcade.key.W, arcade.key.S))
        self._player1_goal = Goal(RESOLUTION[0] * .002, RESOLUTION[1] * .5)
        self._player1_score = 0

        self._player2 = Beater(RESOLUTION[0] * .95, RESOLUTION[1] * .5, keyboard=not ai,
                               keys=(arcade.key.UP, arcade.key.DOWN))
        self._player2_goal = Goal(RESOLUTION[0] * .998, RESOLUTION[1] * .5)
        self._player2_score = 0

        self._ball = Ball(RESOLUTION[0] * .5, RESOLUTION[1] * .5)

        self._heal_list = arcade.SpriteList()

        self._hp_bonus_on_goal = 3
        self._max_score = max_score

        self._spawn_heal_delay_timer = None
        self._spawn_heal_delay_min = 5
        self._spawn_heal_delay_max = 15
        self._cur_heal_delay = randrange(self._spawn_heal_delay_min, self._spawn_heal_delay_max)
        self._ball.restart(RESOLUTION[0] * .5, RESOLUTION[1] * .5)

        self._is_ai_active = ai

    def on_update(self):
        self._player1.update()
        self._player2.update()
        self._player1_goal.update()
        self._player2_goal.update()
        self._ball.update()
        self._sprite_collision()
        self._heal_list.update()
        if self._is_ai_active:
            self._ai()
        self._spawn_heal()
        self._heal_updating()

        if self.is_end_game():
            self._parent_window.set_scene('menu')

    def on_draw(self):
        self._draw_text()
        self._player1.draw()
        self._player2.draw()
        self._player1_goal.draw()
        self._player2_goal.draw()
        self._ball.draw()
        self._heal_list.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self._player1.move_to_y(y)

    def on_mouse_press(self):
        self._player1.stop_moving_on_press()

    def on_mouse_release(self):
        self._player1.continue_moving_on_release()

    def on_key_press(self, key, mod):
        self._player1.on_key_press(key, mod)

        if not self._is_ai_active:
            self._player2.on_key_press(key, mod)

        if key == arcade.key.ESCAPE:
            self._parent_window.set_scene('menu')

    def on_key_release(self, key, mod):
        self._player1.on_key_release(key, mod)

        if not self._is_ai_active:
            self._player2.on_key_release(key, mod)

    def is_end_game(self):
        if self._player1_score == self._max_score or self._player2_score == self._max_score:
            return True
        return False

    def _sprite_collision(self):
        def damage_to_player_by_ball_on_collision(ball, player):
            if player.active and ball.collides_with_sprite(player):
                ball.beat_off()
                player.get_hit_on_collision()
                if player.hp <= 0:
                    player.active = False
                    player.start_timer_to_activate()

        damage_to_player_by_ball_on_collision(self._ball, self._player1)
        damage_to_player_by_ball_on_collision(self._ball, self._player2)

        if self._ball.collides_with_sprite(self._player1_goal):
            self._ball.restart(RESOLUTION[0] * .5, RESOLUTION[1] * .5)
            self._player2_score += 1
            self._player2.hp += self._hp_bonus_on_goal

        if self._ball.collides_with_sprite(self._player2_goal):
            self._ball.restart(RESOLUTION[0] * .5, RESOLUTION[1] * .5)
            self._player1_score += 1
            self._player1.hp += self._hp_bonus_on_goal

        for heal in self._heal_list:
            if self._ball.collides_with_sprite(heal):
                if self._ball.change_x > 0:
                    self._player1.hp += 1
                elif self._ball.change_x < 0:
                    self._player2.hp += 1
                self._heal_list.remove(heal)

    def _draw_text(self):
        arcade.draw_text(f'{self._player1.hp}', RESOLUTION[0] * .005, RESOLUTION[1] * .9,
                         (255, 255, 255), 75)

        arcade.draw_text(f'{self._player2.hp}', RESOLUTION[0] * .97, RESOLUTION[1] * .9,
                         (255, 255, 255), 75)

        arcade.draw_text(f'{self._player1_score} : {self._player2_score}', RESOLUTION[0] * .43, RESOLUTION[1] * .5,
                         (255, 255, 255), 100)

    def _ai(self):
        if self._player2_goal.center_y - self._player2_goal.height / 2 * .8 <= self._ball.center_y \
                <= self._player2_goal.center_y + self._player2_goal.height / 2 * .8:
            self._player2.move_to_y(self._ball.center_y)

    def _spawn_heal(self):
        if self._spawn_heal_delay_timer is None:
            self._spawn_heal_delay_timer = time()
        elif time() - self._spawn_heal_delay_timer >= self._cur_heal_delay:
            self._cur_heal_delay = randrange(self._spawn_heal_delay_min, self._spawn_heal_delay_max)
            self._spawn_heal_delay_timer = time()
            self._heal_list.append(Heal(RESOLUTION[0] * .25, RESOLUTION[0] * .7))

    def _heal_updating(self):
        for heal in self._heal_list:
            if heal.center_y < 0:
                self._heal_list.remove(heal)

