import pygame.image
import skill
import tinhToan


class Minion:
    def __init__(self, ben, x):
        self.img = [pygame.image.load(r"picture\minion\linh1.png"),
                    pygame.image.load(r"picture\minion\linh2.png"),
                    pygame.image.load(r"picture\minion\linh3.png")]
        self.img2 = [pygame.image.load(r"picture\minion\linh1e.png"),
                    pygame.image.load(r"picture\minion\linh2e.png"),
                    pygame.image.load(r"picture\minion\linh3e.png")]
        self.health = 100
        self.range = 40
        self.walkCount = 0
        self.skill = []
        self.health = 10
        self.x = x
        self.y = 250
        self.tonTai = True
        self.hitbox = (self.x, self.y, 200, 200)
        self.ben = ben
        self.vel = 1

    def draw(self, win):

        if self.walkCount == 9:
            self.walkCount = 0

        if self.ben:
            win.blit(self.img2[self.walkCount//3], (self.x, self.y))
        else:
            win.blit(self.img[self.walkCount // 3], (self.x, self.y))
        self.walkCount += 1
    def move(self, ene, minions):
        minx, miny = tinhToan.find(self, ene, minions)
        kc = tinhToan.khoangCach(self.x, self.y, minx, miny)
        if self.ben:
            phia = 1
        else:
            phia = -1
        if kc > self.range:
            self.x += self.vel * phia
        if self.x >= 1300:
            self.x = 1250
        if self.x <= 0:
            self.x = 0
        self.hitbox = (self.x, self.y, 200, 200)

    def hitted(self, enemyskill):
        self.health -= enemyskill.atk
        if self.health <= 0:
            self.tonTai = False