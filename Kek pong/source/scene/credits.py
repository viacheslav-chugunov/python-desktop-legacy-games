import arcade
from ..scene.scene import Scene
from ..config import RESOLUTION


class Credits(Scene):
    def __init__(self, parent):
        super().__init__(arcade.load_texture('media/images/scene/menu/bg.png'), parent)
        self._credits_sprites = arcade.SpriteList()
        self._credits_sprites.append(arcade.Sprite('media/images/scene/credits/contacts.png', 0.5))
        self._credits_sprites.append(arcade.Sprite('media/images/scene/credits/sounds.png', 0.9))
        self._credits_sprites.append(arcade.Sprite('media/images/scene/credits/graphics.png', 0.9))
        self._credits_sprites.append(arcade.Sprite('media/images/scene/credits/soft.png', 0.9))

        start_y = 2.5
        speed = 0.5
        for credit in self._credits_sprites:
            credit.change_y = -speed
            credit.center_x = RESOLUTION[0] * .5
            credit.center_y = RESOLUTION[1] * start_y
            start_y -= 0.4

    def on_update(self):
        self._credits_sprites.update()
        for credit in self._credits_sprites:
            if credit.center_y < -credit.height:
                self._credits_sprites.remove(credit)
        if len(self._credits_sprites) == 0:
            self._parent_window.set_scene('menu')

    def on_draw(self):
        self._credits_sprites.draw()

    def on_key_press(self, key, mod):
        if key == arcade.key.ESCAPE:
            self._parent_window.set_scene('menu')

