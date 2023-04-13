import pygame
import tinhToan
import math
import random
import player


class Enemy:
    def __init__(self):
        self.next_x = 0
        self.next_y = 0
        self.health = 10
        self.tancong = 50
        self.walkCount = 0
        self.thu = 20
        self.skills = []
        self.range = 50
        self.nangluong = 100
        self.hinhanhTrai = [pygame.image.load(r'picture\enemy\L1E.png'),
                            pygame.image.load(r'picture\enemy\L2E.png'),
                            pygame.image.load(r'picture\enemy\L3E.png'),
                            pygame.image.load(r'picture\enemy\L4E.png'),
                            pygame.image.load(r'picture\enemy\L5E.png'),
                            pygame.image.load(r'picture\enemy\L6E.png'),
                            pygame.image.load(r'picture\enemy\L7E.png'),
                            pygame.image.load(r'picture\enemy\L8E.png'),
                            pygame.image.load(r'picture\enemy\L9E.png'),
                            pygame.image.load(r'picture\enemy\L10E.png'),
                            pygame.image.load(r'picture\enemy\L11E.png'),
                            ]
        self.hinhanhPhai = [pygame.image.load(r'picture\enemy\R1E.png'),
                            pygame.image.load(r'picture\enemy\R2E.png'),
                            pygame.image.load(r'picture\enemy\R3E.png'),
                            pygame.image.load(r'picture\enemy\R4E.png'),
                            pygame.image.load(r'picture\enemy\R5E.png'),
                            pygame.image.load(r'picture\enemy\R6E.png'),
                            pygame.image.load(r'picture\enemy\R7E.png'),
                            pygame.image.load(r'picture\enemy\R8E.png'),
                            pygame.image.load(r'picture\enemy\R9E.png'),
                            pygame.image.load(r'picture\enemy\R10E.png'),
                            pygame.image.load(r'picture\enemy\R11E.png'),
                            ]
        self.vel = 2
        self.Q = 0
        self.W = 0
        self.E = 0
        self.x = 100
        self.y = 100
        self.hitbox=(self.x, self.y, 20, 20)
        self.tonTai = True

    def move(self, man, reset):
        if reset % 30 == 0:
            self.next_x, self.next_y = random.randint(man.x, man.x+500), random.randint(man.y, man.y+500)
        else:
            self.x = self.next_x
            self.y = self.next_y
        #minx, miny = tinhToan.find(self, man, minionPlayer)
        kc = tinhToan.khoangCach(self.x, self.y, self.next_x, self.next_y)
        if kc > self.range:
            self.x = int((self.next_x - self.x) * self.vel / kc) + self.x if self.vel < kc else self.next_x
            self.y = int((self.next_y - self.y) * self.vel / kc) + self.y if self.vel < kc else self.next_y

    def draw(self, win):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.x >= self.next_x:
            win.blit(self.hinhanhTrai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.hinhanhPhai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        pygame.draw.rect(win, (0, 128, 0),
                         (self.hitbox[0] - 14, self.hitbox[1] - 22, 50 - (5 * (10 - self.health)), 10))

    # def tanCong(self, loai):
    #     #ramdom de chon loai tan cong

    def hitted(self, enemyskill):
        self.health -= enemyskill.atk
        if self.health <= 0:
            self.tonTai = False