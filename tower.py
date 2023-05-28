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
        if self.tonTai:
            win.blit(self.img, (self.x, self.y))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0] + 65, self.hitbox[1], 50 - (0.05 * (1000 - self.health)), 10))
            pygame.draw.rect(win, color="blue", rect=(self.hitbox[0] + 65, self.hitbox[1], 50, 10), width=2)

    def hitted(self, enemySkill):

        #nha chi bi tan cong boi don danh thuong
        if enemySkill.vel == 8:
            self.health -= enemySkill.atk
            enemySkill.tonTai  = enemySkill.tonTai - 1

            #am thanh
            if self.mau <= 0:
                self.tonTai = False
                #game ket thuc