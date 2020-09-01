import arcade
from ..scene.scene import Scene
from ..config import RESOLUTION


class Menu(Scene):
    def __init__(self, parent):
        super().__init__(arcade.load_texture('media/images/scene/menu/bg.png'), parent)
        self._title_texture = arcade.Sprite('media/images/scene/menu/title.png', 2,
                                            center_x=RESOLUTION[0] * .5, center_y=RESOLUTION[1] * .75)
        self._menu_textures = {
            'new game':
                (arcade.Sprite('media/images/scene/menu/new game.png',
                               center_x=RESOLUTION[0] * .5, center_y = RESOLUTION[1] * .5),
                 arcade.Sprite('media/images/scene/menu/new game_c.png',
                               center_x=RESOLUTION[0] * .5, center_y = RESOLUTION[1] * .5)),
            'duel':
                (arcade.Sprite('media/images/scene/menu/duel.png',
                               center_x=RESOLUTION[0] * .5, center_y = RESOLUTION[1] * .4),
                 arcade.Sprite('media/images/scene/menu/duel_c.png',
                               center_x=RESOLUTION[0] * .5, center_y = RESOLUTION[1] * .4)),
            'credits':
                (arcade.Sprite('media/images/scene/menu/credits.png',
                               center_x=RESOLUTION[0] * .5, center_y = RESOLUTION[1] * .3),
                 arcade.Sprite('media/images/scene/menu/credits_c.png',
                               center_x=RESOLUTION[0] * .5, center_y = RESOLUTION[1] * .3)),
            'exit':
                (arcade.Sprite('media/images/scene/menu/exit.png',
                               center_x=RESOLUTION[0] * .5, center_y = RESOLUTION[1] * .2),
                 arcade.Sprite('media/images/scene/menu/exit_c.png',
                               center_x=RESOLUTION[0] * .5, center_y = RESOLUTION[1] * .2)),
        }
        self.cur_choice = 1

    def on_update(self): pass

    def on_draw(self):
        self._draw_menu()

    def on_key_press(self, key, mod):
        self._menu_controller_on_key_press(key, mod)

    def _menu_controller_on_key_press(self, key, mod):
        if key == arcade.key.W or key == arcade.key.UP:
            if self.cur_choice - 1 >= 1:
                self.cur_choice -= 1
        elif key == arcade.key.S or key == arcade.key.DOWN:
            if self.cur_choice + 1 <= len(self._menu_textures):
                self.cur_choice += 1
        elif key == arcade.key.ENTER:
            if self.cur_choice == 1:
                self._parent_window.set_scene('gameplay')
            elif self.cur_choice == 2:
                self._parent_window.set_scene('duel')
            elif self.cur_choice == 3:
                self._parent_window.set_scene('credits')
            elif self.cur_choice == 4:
                self._parent_window.exit()

    def _draw_menu(self):
        self._title_texture.draw()

        if self.cur_choice != 1:
            self._menu_textures['new game'][0].draw()
        else:
            self._menu_textures['new game'][1].draw()
        if self.cur_choice != 2:
            self._menu_textures['duel'][0].draw()
        else:
            self._menu_textures['duel'][1].draw()
        if self.cur_choice != 3:
            self._menu_textures['credits'][0].draw()
        else:
            self._menu_textures['credits'][1].draw()
        if self.cur_choice != 4:
            self._menu_textures['exit'][0].draw()
        else:
            self._menu_textures['exit'][1].draw()

