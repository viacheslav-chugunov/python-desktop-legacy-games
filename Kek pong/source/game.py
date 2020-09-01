from .window import Window
from .audio import Audio


class Game:
    def __init__(self):
        self._audio = Audio()
        self._window = Window(self._audio)

    def run(self):
        self._window.run()
