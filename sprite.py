# Sprite classes for platform game
import pygame as pg, random, math
from settings import *

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((40, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.speed = 2
        self.gocDiChuyen = self.changeHuongDi()

    def changeHuongDi(self):
        mylist = [1, 2, 3, 4, 5, 6]
        myRan = random.choices(mylist, weights=[1, 4, 1, 1, 4, 1], k=1)
        gocDiChuyenRandom = 0
        if myRan[0] == 5:
            gocDiChuyenRandom = random.randint(-60, -20)
        elif myRan[0] == 2:
            gocDiChuyenRandom = random.randint(20, 60)
        elif myRan[0] == 3:
            gocDiChuyenRandom = random.randint(61, 90)
        elif myRan[0] == 1:
            gocDiChuyenRandom = random.randint(0, 19)
        elif myRan[0] == 4:
            gocDiChuyenRandom = random.randint(-19, 0)
        elif myRan[0] == 6:
            gocDiChuyenRandom = random.randint(-90, -61)
        return gocDiChuyenRandom

    def move(self):
        self.pos.x += self.speed
        self.pos.y += math.tan(math.radians(self.gocDiChuyen)) * self.speed

    def update(self):

        # apply friction
        # self.acc.x += self.vel.x * PLAYER_FRICTION
        # # equations of motion
        # self.vel += self.acc
        # self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH - 30:
            self.gocDiChuyen = self.changeHuongDi()
        if self.pos.x < 20:
            self.gocDiChuyen = self.changeHuongDi()
        if self.pos.y > HEIGHT - 30:
            self.gocDiChuyen = self.changeHuongDi()
        if self.pos.y < 20:
            self.gocDiChuyen = self.changeHuongDi()

        self.rect.center = self.pos


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
