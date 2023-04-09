import pygame
import math
import tinhToan
import skill



class Player:
    def __init__(self):
        self.next_x = 0
        self.next_y = 0
        self.mau = 1000
        self.tancong = 50
        self.walkCount = 0
        self.thu = 20
        self.range = 200
        self.skills = []
        self.hitbox = (self.x, self.y, 20, 20)
        self.nangluong = 100
        self.hinhanhTrai = [pygame.image.load(r'picture\main character\R1.png'), pygame.image.load(r'picture\main character\R2.png'), pygame.image.load(r'picture\main character\R3.png'), pygame.image.load(r'picture\main character\R4.png'), pygame.image.load(r'picture\main character\R5.png'), pygame.image.load(r'picture\main character\R6.png'),pygame.image.load(r'picture\main character\R7.png'), pygame.image.load(r'picture\main character\R8.png'), pygame.image.load(r'picture\main character\R9.png')]
        self.hinhanhPhai = [pygame.image.load(r'picture\main character\L1.png'), pygame.image.load(r'picture\main character\L2.png'), pygame.image.load(r'picture\main character\L3.png'), pygame.image.load(r'picture\main character\L4.png'), pygame.image.load(r'picture\main character\L5.png'), pygame.image.load(r'picture\main character\L6.png'), pygame.image.load(r'picture\main character\L7.png'), pygame.image.load(r'picture\main character\L8.png'), pygame.image.load(r'picture\main character\L9.png')]
        self.vel = 3
        self.Q = 0
        self.W = 0
        self.E = 0
        self.x = 100
        self.y = 100
        self.tonTai = True

    def move(self,next_x, next_y,change):
        if change:
            self.next_x = next_x
            self.next_y = next_y
        kc = tinhToan.khoangCach(self.x, self.y, self.next_x, self.next_y)
        self.x = int((self.next_x - self.x) * self.vel / kc) + self.x if self.vel < kc else self.next_x
        self.y = int((self.next_y - self.y) * self.vel / kc) + self.y if self.vel < kc else self.next_y



    def draw(self,win):
        self.walkCount = self.walkCount + 1 if self.walkCount < 26 else 0
        if self.next_x > self.x:
            win.blit(self.hinhanhTrai[self.walkCount // 3], (self.x-25, self.y-25))
        else:
            win.blit(self.hinhanhPhai[self.walkCount // 3], (self.x-25, self.y-25))








    def skill1(self, win, start_x, start_y, end_x, end_y):
        self.Q = 0
        self.skills.append(skill.Skill([pygame.image.load(r"picture/main character/skills/skill1.png")], 100, start_x, start_y, end_x, end_y, 200, 1, (self.x, self.y, 10, 10)))


    def skill2(self, win, start_x, start_y, end_x, end_y):
        self.skills.append(skill.Skill([pygame.image.load(r"picture/main character/skills/skill2.png"), pygame.image.load(r"picture/main character/skills/skill2.png"),
                                        pygame.image.load(r"picture/main character/skills/skill2.png"), pygame.image.load(r"picture/main character/skills/skill2.png"),
                                       pygame.image.load(r"picture/main character/skills/skill2.png"), pygame.image.load(r"picture/main character/skills/skill2.png")], 200, start_x, start_y, end_x,
                        end_y, 200, 6,(self.x, self.y, 10, 10)))
        self.W = 0


    def ultilmate(self, win, start_x, start_y, end_x, end_y):
        self.skills.append(skill.Skill([pygame.image.load(r"picture/main character/skills/util.png")], 150, end_x, end_y, end_x, end_y, 300, 1, (self.x ,self.y ,10 ,10)))
        self.E = 0


    def attack(self, win, skill, start_x, start_y, end_x, end_y):
        if skill == "Q":
            self.skill1(win, start_x, start_y, end_x, end_y)
        elif skill == "W":
            self.skill2(win, start_x, start_y, end_x, end_y)
        elif skill == "E":
            self.ultimate(win, start_x, start_y, end_x, end_y)


    def hitted(self, enemyskill):
        if self.hitbox[1] < enemyskill.hitbox[1]:



