import pygame.image

import calculator
import skill
import autoSkill


class Turret:
    def __init__(self, img, x, y):
        self.health = 1000
        self.img = img
        self.atk = 50
        self.skills = None
        self.imgatk = pygame.image.load(r"picture/main character/skills/skill1.png")
        self.x = x
        self.y = y
        self.cho = 0
        self.hitbox = (self.x, self.y, 150, 150)
        self.tonTai = True
        self.range = 100
        self.status = False  # true neu tru sap tan cong nguoi choi, flase neu khong

    def draw(self, win):


        if self.status:
            pygame.draw.ellipse(win, color="red", rect=(self.x - 70, self.y + 50, 240, 170), width=2)
        else:
            pygame.draw.ellipse(win, color="green", rect=(self.x - 70, self.y + 50, 240, 170), width=2)
        win.blit(self.img, (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0),
                         (self.hitbox[0] + 15, self.hitbox[1] - 22, 50 - (0.05 * (1000 - self.health)), 10))
        pygame.draw.rect(win, color="blue", rect = (self.hitbox[0] + 15, self.hitbox[1] - 22, 50, 10), width = 2)


    def attack(self, ene, minions):
        self.cho = 0 if self.cho <= 0 else self.cho - 1
        self.status = False
        for i in minions:
            if calculator.checkInsideEclip(self.x + 50, self.y + 135, i.x, i.y, 120, 85):
                if self.cho == 0:
                    self.cho = 100
                    self.skills = autoSkill.AutoSkill([self.imgatk], 50, self.x, self.y, i, 220, 1)
                return
        if calculator.checkInsideEclip(self.x + 50, self.y + 135, ene.x, ene.y, 120, 85):
            if self.cho == 0:
                self.cho = 100
                print("tan cong")
                self.skills = autoSkill.AutoSkill([self.imgatk], 50, self.x, self.y, ene, 220, 1)

            self.status = True
            return



    def hitted(self, enemyskill):
        self.mau -= enemyskill.atk
        #am thanh
        if self.mau <= 0:
            self.tonTai = False
            #game ket thuc