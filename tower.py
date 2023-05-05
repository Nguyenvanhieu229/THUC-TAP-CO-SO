import pygame.draw

import skill


class Tower:
    def __init__(self, img, x, y):
        self.health = 1000
        self.range = 300
        self.img = img
        self.x = x
        self.y = y
        self.tonTai = True

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


    def hitted(self, chiSo):
        self.mau -= chiSo
        #am thanh
        if self.mau <= 0:
            self.tonTai = False
            #game ket thuc