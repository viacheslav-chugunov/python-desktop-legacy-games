class Score:
    def __init__(self, based=0):
        self.score = based
        self.__adding = True

    def increase(self, inc=1):
        if self.__adding:
            self.score += inc

    def stop(self):
        self.__adding = False
