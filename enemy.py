import pygame

import autoSkill
import calculator
import math
import random
import player
import skill
import not_move_skill


class Enemy:
    def __init__(self):
        self.next_x = 0
        self.next_y = 0
        self.health = 500
        self.tancong = 100
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
        self.A = 0
        self.x = 1300
        self.y = 100
        self.hitbox = (self.x, self.y, 50, 50)
        self.tonTai = True
        self.dead = pygame.image.load(r"picture/deadPic.png")
        self.lv = 1
        self.maxExp = 100
        self.exp = 0

    def move(self, man, reset, minionPlayer, blueTurret, blueTower):

        dich = self.chonMucTieuDi(man, minionPlayer, blueTurret, blueTower)

        kcDich = calculator.khoangCach(self.x, self.y, dich.x, dich.y)

        if reset % 2 == 0 and dich:
            self.next_x =  random.randint(int(dich.x - 30), int(dich.x + 30))
            self.next_y =  random.randint(int(dich.y - 30), int(dich.y + 30))
        kc = calculator.khoangCach(self.x, self.y, self.next_x, self.next_y)

        if kcDich > self.range:
            self.x = ((self.next_x - self.x) * self.vel / kc) + self.x if self.vel < kc else self.x
            self.y = ((self.next_y - self.y) * self.vel / kc) + self.y if self.vel < kc else self.y

        self.hitbox = (self.x, self.y, 20, 20)

    def draw(self, win):

        if self.health <= 0:
            win.blit(self.dead,(self.x, self.y))
            return

        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.x >= self.next_x:
            win.blit(self.hinhanhTrai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.hinhanhPhai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        pygame.draw.rect(win, (255, 0, 0),
                         (self.hitbox[0]+15, self.hitbox[1] - 5 , 50 - (0.1 * (500 - self.health)), 10))
        pygame.draw.rect(win, color="blue", rect=(self.hitbox[0]+15, self.hitbox[1] - 5, 50, 10), width=2)
        font3 = pygame.font.SysFont("comicsans", 20, True)
        text = font3.render(str(self.lv), 1, (0, 0, 0))
        pygame.draw.circle(win, color="red", center=(self.hitbox[0]+2, self.hitbox[1]), radius=12, width=0)
        win.blit(text, (self.x - 27 + 23, self.y - 34 + 20))



    def hitted(self, sk):
        if self.health > 0 and sk.tonTai > 0:
            self.health -= sk.atk
            sk.tonTai = sk.tonTai - 1

        if self.health <= 0:
            self.tonTai = False

    def skill1(self, win, start_x, start_y, end_x, end_y):
        self.Q = 100
        self.skills.append(skill.Skill([pygame.image.load(r"picture/enemy/skill1.png")], 80, start_x, start_y, end_x, end_y, 200, 1))


    def skill2(self, win, start_x, start_y, end_x, end_y):
        self.skills.append(skill.Skill([pygame.image.load(r"picture/enemy/skill2.png")], 100, start_x, start_y, end_x,
                        end_y, 200, 1))
        self.W = 150


    def ultimate(self, win, start_x, start_y, end_x, end_y):
        self.E = 240
        self.skills.append(
            not_move_skill.NotMoveSkill([pygame.image.load(r"picture/enemy/utilmate.png")], 10, end_x,
                                        end_y, 100, 1, 120))

    def chonMucTieu(self, nhanVat, linhs, turret, tower):

        for linh in linhs:
            kc = calculator.khoangCach(self.x, self.y, linh.x, linh.y)
            if kc < self.range:
                return linh

        kc = calculator.khoangCach(self.x, self.y, nhanVat.x, nhanVat.y)
        if kc < self.range:
            return nhanVat

        kc = calculator.khoangCach(self.x, self.y, turret.x, turret.y)
        if kc < self.range:
            return turret

        kc = calculator.khoangCach(self.x, self.y, tower.x, tower.y)
        if kc < self.range and turret.health <= 0:
            return tower

    def chonMucTieuDi(self, nhanVat, linhs, turret, tower):

        if nhanVat.health > 0:
            return nhanVat

        for linh in linhs:
            return linh

        if turret.health > 0:
            return turret

        if tower.health > 0:
            return tower

    def danhThuong(self, nhanVat, minions, turret, tower):

        dich = self.chonMucTieu(nhanVat, minions, turret, tower)
        # them moi doi tuong autoSkill vao mang skill cua linh
        if dich:
            if dich.health <= 0:
                return
            self.A = 45
            self.skills.append(
                autoSkill.AutoSkill([pygame.image.load(r"picture/enemy/danhthuong .png")], self.tancong, self.x, self.y, dich, 200, 1))

    def attack(self, win, skill, start_x, start_y, end_x, end_y):

        if self.health <= 0:
            return

        if skill == "Q":
            self.skill1(win, start_x, start_y, end_x, end_y)
        elif skill == "W":
            self.skill2(win, start_x, start_y, end_x, end_y)
        elif skill == "E":
            self.ultimate(win, start_x, start_y, end_x, end_y)