import pygame.image

import calculator
import skill
import autoSkill


class Turret:
    def __init__(self, img, x, y):
        self.health = 1000
        self.img = img
        self.atk = 50
        self.skills = []
        self.imgatk = pygame.image.load(r"picture/main character/skills/skill1.png")
        self.x = x
        self.y = y
        self.cho = 0
        self.hitbox = (self.x, self.y, 150, 150)
        self.tonTai = True
        self.range = 100
        self.status = False  # true neu tru sap tan cong nguoi choi, flase neu khong

    def draw(self, win):

        if self.health > 0 :
            if self.status:
                pygame.draw.ellipse(win, color="red", rect=(self.x - 70, self.y + 50, 240, 170), width=2)
            else:
                pygame.draw.ellipse(win, color="green", rect=(self.x - 70, self.y + 50, 240, 170), width=2)

            # ve hinh anh Tru neu tru con ton tai
            if self.tonTai:
                color = (255, 0, 0) if self.x == 1008 and self.y == 125 else (126, 248, 5)
                win.blit(self.img, (self.x, self.y))
                pygame.draw.rect(win, color,
                                 (self.hitbox[0] + 15, self.hitbox[1] - 22, 50 - (0.05 * (1000 - self.health)), 10))
                pygame.draw.rect(win, color="blue", rect = (self.hitbox[0] + 15, self.hitbox[1] - 22, 50, 10), width = 2)

    def chonMucTieu(self, ene, minions):

        for i in minions:
            if calculator.checkInsideEclip(self.x + 50, self.y + 135, i.x, i.y, 120, 85) and i.health > 0:
                return i

        if calculator.checkInsideEclip(self.x + 50, self.y + 135, ene.x, ene.y, 120, 85) and ene.health > 0:
            self.status = True
            return ene


    def attack(self, ene, minions):
        #xu ly thoi gian cho trung chieu
        if self.health <= 0:
            return
        self.cho = 0 if self.cho <= 0 else self.cho - 1
        self.status = False

        dich = self.chonMucTieu(ene, minions)
        if dich and self.cho == 0:
                self.cho = 45
                self.skills.append(autoSkill.AutoSkill([pygame.image.load(r"picture/skill1.JPG-removebg-preview.png")], 100,
                                   self.x + 20, self.y + 20, dich, 200, 1))

    def hitted(self, enemySkill):
        #tru chi bi tan cong boi don danh thuong
        if self.health > 0:
            if enemySkill.vel == 8:
                self.health -= enemySkill.atk
                enemySkill.tonTai = enemySkill.tonTai -1

                # am thanh
        if self.health <= 0:
            self.tonTai = False
                # game ket thuc