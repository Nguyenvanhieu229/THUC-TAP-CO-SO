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
        self.hitbox = (self.x, self.y, 150, 150)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


    def hitted(self, enemySkill):
        #nha chi bi tan cong boi don danh thuong
        if enemySkill.vel == 8:
            self.mau -= enemySkill.atk

            #am thanh
            if self.mau <= 0:
                self.tonTai = False
                #game ket thuc