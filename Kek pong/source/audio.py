import arcade
from random import randint
from time import time


class Audio:
    def __init__(self):
        self._sounds = (
            (arcade.Sound('media/sound/Chill Gaming.mp3'), 188),
            (arcade.Sound('media/sound/Done With Work.mp3'), 198),
            (arcade.Sound('media/sound/Homework.mp3'), 213),
            (arcade.Sound('media/sound/I Got This.mp3'), 197),
            (arcade.Sound('media/sound/On My Own.mp3'), 200),
        )
        self._cur_sound_index = randint(0, len(self._sounds) - 1)
        self._cur_sound = self._sounds[self._cur_sound_index]
        self._sound_swap_delay_timer = None
        self._time_to_next_song = None

    def play(self):
        self._cur_sound[0].play()
        self._sound_swap_delay_timer = time()
        self._time_to_next_song = self._cur_sound[1]

    def song_updating(self):
        if self._sound_swap_delay_timer is not None:
            song_interval_s = 3
            if time() - self._sound_swap_delay_timer >= self._time_to_next_song + song_interval_s:
                self._cur_sound_index = self._get_new_cur_sound_index()
                self._cur_sound = self._sounds[self._cur_sound_index]
                self.play()

    def _get_new_cur_sound_index(self):
        """Using only if self._sounds len > 1"""
        index = randint(0, len(self._sounds) - 1)
        if index == self._cur_sound_index:
            return self._get_new_cur_sound_index()
        return index
