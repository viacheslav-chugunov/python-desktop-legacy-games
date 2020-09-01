import arcade


class Goal(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('media/images/sprite/goal.png', 5, center_x=x, center_y=y)
