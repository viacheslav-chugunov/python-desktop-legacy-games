import arcade
from .config import RESOLUTION, WINDOW_SETUP
from .scene.menu import Menu
from .scene.gameplay import Gameplay
from .scene.credits import Credits


class Window(arcade.Window):
    def __init__(self, audio=None):
        super().__init__(*RESOLUTION, **WINDOW_SETUP)
        self._audio = audio
        self.set_mouse_visible(False)
        self._menu_scene = Menu(self)
        self.cur_scene = self._menu_scene
        if self._audio:
            self._audio.play()

    def run(self):
        arcade.run()

    def on_update(self, delta_time):
        self.cur_scene.on_update()
        if self._audio:
            self._audio.song_updating()

    def on_draw(self):
        arcade.start_render()
        self.cur_scene.on_draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cur_scene.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        self.cur_scene.on_mouse_press()

    def on_mouse_release(self, x, y, button, modifiers):
        self.cur_scene.on_mouse_release()

    def on_key_press(self, key, modifiers):
        self.cur_scene.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.cur_scene.on_key_release(key, modifiers)

    def set_scene(self, scene: str):
        if scene == 'menu':
            self.cur_scene = self._menu_scene
        elif scene == 'gameplay':
            self.cur_scene = Gameplay(self)
        elif scene == 'duel':
            self.cur_scene = Gameplay(self, ai=False)
        elif scene == 'credits':
            self.cur_scene = Credits(self)
        self._menu_scene.cur_choice = 1

    def exit(self):
        arcade.quick_run(0)

