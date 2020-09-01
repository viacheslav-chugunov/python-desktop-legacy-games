import pygame


class Status:
    def __init__(self):
        pygame.font.init()
        self.player_speed_label = pygame.Surface((200, 50))
        self.player_speed_font = pygame.font.Font(None, 30)

        self.took = 0
        self.took_label = pygame.Surface((400, 50))
        self.took_font = pygame.font.Font(None, 30)

        self.pause_label = pygame.Surface((500, 90))
        self.pause_font = pygame.font.Font(None, 70)

        self.lost_label = pygame.Surface((500, 90))
        self.lost_font = pygame.font.Font(None, 70)
