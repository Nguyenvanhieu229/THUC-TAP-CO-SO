import pygame.image

import autoSkill
import not_move_skill
import skill
import calculator


class Minion:
    def __init__(self, ben, x, y):
        self.img = [pygame.image.load(r"picture\minion\redphai-removebg-preview.png"),
                    pygame.image.load(r"picture\minion\redthang-removebg-preview.png"),
                    pygame.image.load(r"picture\minion\redtrai-removebg-preview.png")]
        self.img2 = [pygame.image.load(r"picture\minion\bluephai.png"),
                     pygame.image.load(r"picture\minion\bluethang.png"),
                     pygame.image.load(r"picture\minion\bluetrai.png")]
        self.range = 50
        self.walkCount = 0
        self.skills = []
        self.health = 500
        self.x = x
        self.y = y
        self.tonTai = 1
        self.hitbox = (self.x, self.y, 30, 30)
        self.ben = ben
        self.vel = 2
        self.cho = 0
        self.next_x = 1239 if ben else 153
        self.next_y = 151 if ben else 623
        self.timeExist = 60 if not self.tonTai else 0
        self.lvup = pygame.font.SysFont("comicsans", 15, True)

    def draw(self, win):

        if self.walkCount == 15:
            self.walkCount = 0

        if self.ben:
            win.blit(self.img2[self.walkCount//5], (self.x, self.y))
            pygame.draw.rect(win, (126, 248, 5),
                             (self.hitbox[0], self.hitbox[1] - 22, 50 - (0.1 * (500 - self.health)), 10))
            pygame.draw.rect(win, color="blue", rect=(self.hitbox[0], self.hitbox[1] - 22, 50, 10), width=2)
        else:
            win.blit(self.img[self.walkCount // 5], (self.x, self.y))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0], self.hitbox[1] - 22, 50 - (0.1 * (500 - self.health)), 10))
            pygame.draw.rect(win, color="blue", rect=(self.hitbox[0], self.hitbox[1] - 22, 50, 10), width=2)
        self.walkCount += 1


    def move(self, ene, minions,turret):
        minx, miny = calculator.find(self, ene, minions, turret)
        kcDich = calculator.khoangCach(self.x, self.y, minx, miny)
        kc = calculator.khoangCach(self.x, self.y, self.next_x, self.next_y)

        if kcDich > self.range:
            self.x = ((self.next_x - self.x) * self.vel / kc) + self.x if self.vel < kc else self.x
            self.y = ((self.next_y - self.y) * self.vel / kc) + self.y if self.vel < kc else self.y

        self.hitbox = (self.x, self.y, 20, 20)

    def chonMucTieu(self, nhanVat, linhs, turret, tower):

        for linh in linhs:
            kc = calculator.khoangCach(self.x, self.y, linh.x, linh.y)
            if kc < self.range:
                return linh

        kc = calculator.khoangCach(self.x, self.y, nhanVat.x, nhanVat.y)
        if kc < self.range:
            return nhanVat

        kc = calculator.khoangCach(self.x, self.y, turret.x, turret.y)
        if kc < self.range and turret.health > 0:
            return turret

        kc = calculator.khoangCach(self.x, self.y, tower.x, tower.y)
        if kc < self.range and tower.health > 0:
            return tower

    def attack(self, nhanVat, minions, turret, tower ):
        if self.health <= 0:
            return
        # xu ly thoi gian cho
        self.cho = self.cho - 1 if self.cho >= 1 else 0

        if self.cho > 0:
            return

        dich = self.chonMucTieu(nhanVat, minions, turret, tower)
        # them moi doi tuong autoSkill vao mang skill cua linh
        if dich:
            if dich.health <= 0:
                return
            self.cho = 45
            self.skills.append(autoSkill.AutoSkill([pygame.image.load(r"picture/hong.png") if self.ben else pygame.image.load(r"picture/nau.png")], 30, self.x, self.y, dich, 200, 1))

    def hitted(self, enemyskill):
        if self.health > 0 and enemyskill.tonTai > 0:
            self.health -= enemyskill.atk
            enemyskill.tonTai = enemyskill.tonTai - 1

        if self.health <= 0:
            self.tonTai = 0