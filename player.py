import pygame
import math

import autoSkill
import calculator
import not_move_skill
import skill



class Player:
    def __init__(self):
        self.next_x = 100
        self.next_y = 700
        self.health = 1000
        self.tancong = 500
        self.walkCount = 0

        self.health = 500
        self.thu = 20
        self.range = 200
        self.skills = []
        self.nangluong = 100
        self.hinhanhTrai = [pygame.image.load(r'picture\main character\R1.png'), pygame.image.load(r'picture\main character\R2.png'), pygame.image.load(r'picture\main character\R3.png'), pygame.image.load(r'picture\main character\R4.png'), pygame.image.load(r'picture\main character\R5.png'), pygame.image.load(r'picture\main character\R6.png'),pygame.image.load(r'picture\main character\R7.png'), pygame.image.load(r'picture\main character\R8.png'), pygame.image.load(r'picture\main character\R9.png')]
        self.hinhanhPhai = [pygame.image.load(r'picture\main character\L1.png'), pygame.image.load(r'picture\main character\L2.png'), pygame.image.load(r'picture\main character\L3.png'), pygame.image.load(r'picture\main character\L4.png'), pygame.image.load(r'picture\main character\L5.png'), pygame.image.load(r'picture\main character\L6.png'), pygame.image.load(r'picture\main character\L7.png'), pygame.image.load(r'picture\main character\L8.png'), pygame.image.load(r'picture\main character\L9.png')]
        self.vel = 5
        self.choHoiSinh = 0
        self.Q = 0
        self.W = 0
        self.E = 0
        self.A = 0
        self.x = 100
        self.y = 700
        self.hitbox = (self.x, self.y, 20, 20)
        self.tonTai = True
        self.dead = pygame.image.load(r"picture/deadPic.png")
        self.lv = 1
        self.maxExp = 100
        self.exp = 0

    def move(self, next_x, next_y, change):
        if change:
            self.next_x = next_x
            self.next_y = next_y
        kc = calculator.khoangCach(self.x, self.y, self.next_x, self.next_y)
        self.x = int((self.next_x - self.x) * self.vel / kc) + self.x if self.vel < kc else self.next_x
        self.y = int((self.next_y - self.y) * self.vel / kc) + self.y if self.vel < kc else self.next_y
        self.hitbox = (self.x, self.y, 200, 200)



    def draw(self,win):
        if self.health <= 0:
            win.blit(self.dead,(self.x, self.y))
            return

        self.walkCount = self.walkCount + 1 if self.walkCount < 26 else 0
        if self.next_x > self.x:
            win.blit(self.hinhanhTrai[self.walkCount // 3], (self.x-25, self.y-25))
        else:
            win.blit(self.hinhanhPhai[self.walkCount // 3], (self.x-25, self.y-25))
        pygame.draw.rect(win, (126, 248, 5),
                         (self.hitbox[0] - 10, self.hitbox[1] - 22, 50 - (0.1 * (500 - self.health)), 10))
        pygame.draw.rect(win, color="blue", rect=(self.hitbox[0]-10, self.hitbox[1] - 22, 50, 10), width=2)
        font3 = pygame.font.SysFont("comicsans", 20, True)
        text = font3.render(str(self.lv), 1, (0, 0, 0))
        pygame.draw.circle(win, color="green", center=(self.hitbox[0] - 22, self.hitbox[1] - 19), radius=12,width = 0)
        win.blit(text, (self.x-27, self.y-34))

    def danhThuong(self,target):
        if target.health <= 0:
            return
        self.A = 50
        self.skills.append(autoSkill.AutoSkill([pygame.image.load(r"picture/main character/skills/danhThuong.png")],self.tancong,self.x,self.y
                                                    , target, 100, 1))

    def skill1(self, win, start_x, start_y, end_x, end_y):
        self.Q = 100
        self.skills.append(skill.Skill([pygame.image.load(r"picture/main character/skills/skill1a.png")], 30, start_x, start_y, end_x, end_y, 200, 1))

    def skill2(self, win, start_x, start_y, end_x, end_y):
        self.skills.append(skill.Skill([pygame.image.load(r"picture/main character/skills/skill2a.png")], 50, start_x, start_y, end_x, end_y, 200, 1))
        self.W = 150

    def ultimate(self, end_x, end_y):
        self.x = end_x + 75
        self.y = end_y + 80
        self.next_x = end_x + 75
        self.next_y = end_y + 80
        self.E = 240
        self.skills.append(not_move_skill.NotMoveSkill([pygame.image.load(r"picture/main character/skills/skill3a.png")], 100, end_x, end_y, 100, 1, 30))

    def attack(self, win, skill, start_x, start_y, end_x, end_y):

        if skill == "Q":
            self.skill1(win, start_x, start_y, end_x, end_y)
        elif skill == "W":
            self.skill2(win, start_x, start_y, end_x, end_y)
        elif skill == "E":
            self.ultimate(end_x, end_y)

    def hitted(self, enemyskill):

        if self.health > 0 and enemyskill.tonTai > 0:
            self.health -= enemyskill.atk
            enemyskill.tonTai = enemyskill.tonTai - 1

        if self.health <= 0:
            self.tonTai = False





