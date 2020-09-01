import pygame


class Score:
    def __init__(self, based=0):
        pygame.font.init()
        self.count = based
        self.label = pygame.Surface((200, 50))
        self.font = pygame.font.Font(None, 30)

    def update(self, add=1):
        self.count += add
