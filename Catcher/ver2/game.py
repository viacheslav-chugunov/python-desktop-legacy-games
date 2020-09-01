import pygame
import math
from player import Player
from falling import Falling
from score import Score
from status import Status


class Game:
    def __init__(self, width, height, title):
        self.WIDTH = width
        self.HEIGHT = height
        self.TITLE = title
        self.BG_COLOR = (153, 204, 255)
        pygame.font.init()
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        pygame.display.set_icon(pygame.image.load("images/falling.png"))
        self.running = True
        self.pause = True
        self.lost = False
        self.player = Player(self.WIDTH / 2, self.HEIGHT * .9, self.WIDTH, self.HEIGHT)
        self.player_speed = 2.0
        self.falling = [Falling(0, self.WIDTH, self.HEIGHT, 0.3)]
        self.score = Score()
        self.status = Status()
        pygame.mixer.init()
        self.audio = pygame.mixer.Sound("music/bg.ogg")
        self.audio.play(-1)

    def run(self):
        while self.running:
            self.screen.fill(self.BG_COLOR)
            self.score.label.fill(self.BG_COLOR)
            self.status.player_speed_label.fill(self.BG_COLOR)
            self.status.took_label.fill(self.BG_COLOR)
            self.status.pause_label.fill(self.BG_COLOR)
            self.status.lost_label.fill(self.BG_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.audio.stop()

                self.__key_controller(event)

            if not self.pause and not self.lost:
                self.__update()

            self.__draw()
            self.__collision()
            pygame.display.update()

    def __key_controller(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.speed_x = -self.player_speed
            if event.key == pygame.K_RIGHT:
                self.player.speed_x = self.player_speed

            if event.key == pygame.K_p:
                if self.pause:
                    self.pause = False
                else:
                    self.pause = True

            if not self.lost:
                if event.key == pygame.K_1 and self.score.count >= 20:
                    self.falling.append(Falling(0, self.WIDTH, self.HEIGHT, 0.3))
                    self.score.count -= 20
                if event.key == pygame.K_2 and self.score.count >= 10:
                    if self.player_speed + 0.5 <= 5:
                        self.player_speed += 0.5
                        self.score.count -= 10
                if event.key == pygame.K_3 and self.score.count >= 50:
                    for falling in self.falling:
                        falling.speed_y = 0.05
                    self.score.count -= 50

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player.speed_x = 0
            if event.key == pygame.K_RIGHT:
                self.player.speed_x = 0

    def __draw(self):
        if not self.lost:
            self.status.player_speed_label.blit(
                self.status.player_speed_font.render("Player speed: " + str(self.player_speed), 1, (0, 0, 0)), (10, 10))
            self.status.took_label.blit(
                self.status.took_font.render("Cookies collected: " + str(self.status.took), 1, (0, 0, 0)), (10, 10))
            self.status.pause_label.blit(self.status.pause_font.render('Press "P" to resume', 1, (0, 0, 0)), (10, 10))
            self.score.label.blit(self.score.font.render("Count: " + str(self.score.count), 1, (0, 0, 0)), (10, 10))
            self.screen.blit(self.status.took_label, (self.WIDTH * .8, 50))
            self.screen.blit(self.status.player_speed_label, (self.WIDTH * .8, 0))
            if self.pause:
                self.screen.blit(self.status.pause_label, (self.WIDTH * .3, self.HEIGHT * .4))
            self.screen.blit(self.score.label, (0, 0))
            self.screen.blit(self.player.image, (self.player.x, self.player.y))
            for falling in self.falling:
                self.screen.blit(falling.image, (falling.x, falling.y))
        else:
            self.status.lost_label.blit(self.status.lost_font.render("Total: " + str(self.score.count), 1, (0, 0, 0)), (10, 10))
            self.screen.blit(self.status.lost_label, (self.WIDTH * .4, self.HEIGHT * .4))

    def __update(self):
        self.player.update()
        for falling in self.falling:
            falling.update()

    def __collision(self):
        for falling in self.falling:
            distance_x = math.sqrt((math.pow(self.player.x - falling.x, 2)))
            distance_y = math.sqrt(math.pow(self.player.y - falling.y, 2))
            if distance_x <= 186 and distance_y <= 69:
                falling.restart(0.01)
                self.score.update()
                self.status.took += 1
                self.__additional()
            elif falling.y > self.HEIGHT + 35:
                self.falling.remove(falling)
                del falling
                self.score.update(-10)
                if len(self.falling) == 0:
                    self.score.update(10)
                    self.lost = True

    def __additional(self):
        if self.score.count == 10:
            self.score.count += 20
            self.falling.append(Falling(0, self.WIDTH, self.HEIGHT, 0.3))
        elif self.score.count == 70:
            self.score.count += 40
            self.falling.append(Falling(0, self.WIDTH, self.HEIGHT, 0.3))
        elif self.score.count == 150:
            self.score.count += 80
            self.falling.append(Falling(0, self.WIDTH, self.HEIGHT, 0.3))
        elif self.score.count == 250:
            self.score.count += 130
            self.falling.append(Falling(0, self.WIDTH, self.HEIGHT, 0.3))
        elif self.score.count == 500:
            self.score.count += 230
            self.falling.append(Falling(0, self.WIDTH, self.HEIGHT, 0.3))
        elif self.score.count == 850:
            self.score.count += 400
            self.falling.append(Falling(0, self.WIDTH, self.HEIGHT, 0.3))
        elif self.score.count == 1500:
            self.score.count += 800
            self.falling.append(Falling(0, self.WIDTH, self.HEIGHT, 0.3))
        elif self.score.count == 2500:
            self.score.count += 1500
            self.falling.append(Falling(0, self.WIDTH, self.HEIGHT, 0.3))
