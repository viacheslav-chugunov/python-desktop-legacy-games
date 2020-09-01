from abc import ABC, abstractmethod


class Scene(ABC):
    def __init__(self, bg_texture, parent_window):
        self.bg_texture = bg_texture
        self._parent_window = parent_window

    @abstractmethod
    def on_update(self): pass

    @abstractmethod
    def on_draw(self): pass

    def on_mouse_motion(self, x, y, dx, dy): pass

    def on_mouse_press(self): pass

    def on_mouse_release(self): pass

    def on_key_press(self, key, mod): pass