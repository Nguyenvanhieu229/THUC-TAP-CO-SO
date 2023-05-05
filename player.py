import pygame
import math
import calculator
import skill



class Player:
    def __init__(self):
        self.next_x = 100
        self.next_y = 700
        self.health = 1000
        self.tancong = 50
        self.walkCount = 0
        self.health = 500
        self.thu = 20
        self.range = 200
        self.skills = []
        self.nangluong = 100
        self.hinhanhTrai = [pygame.image.load(r'picture\main character\R1.png'), pygame.image.load(r'picture\main character\R2.png'), pygame.image.load(r'picture\main character\R3.png'), pygame.image.load(r'picture\main character\R4.png'), pygame.image.load(r'picture\main character\R5.png'), pygame.image.load(r'picture\main character\R6.png'),pygame.image.load(r'picture\main character\R7.png'), pygame.image.load(r'picture\main character\R8.png'), pygame.image.load(r'picture\main character\R9.png')]
        self.hinhanhPhai = [pygame.image.load(r'picture\main character\L1.png'), pygame.image.load(r'picture\main character\L2.png'), pygame.image.load(r'picture\main character\L3.png'), pygame.image.load(r'picture\main character\L4.png'), pygame.image.load(r'picture\main character\L5.png'), pygame.image.load(r'picture\main character\L6.png'), pygame.image.load(r'picture\main character\L7.png'), pygame.image.load(r'picture\main character\L8.png'), pygame.image.load(r'picture\main character\L9.png')]
        self.vel = 5
        self.Q = 0
        self.W = 0
        self.E = 0
        self.x = 100
        self.y = 700
        self.hitbox = (self.x, self.y, 20, 20)
        self.tonTai = True

    def move(self,next_x, next_y,change):
        if change:
            self.next_x = next_x
            self.next_y = next_y
        kc = calculator.khoangCach(self.x, self.y, self.next_x, self.next_y)
        self.x = int((self.next_x - self.x) * self.vel / kc) + self.x if self.vel < kc else self.next_x
        self.y = int((self.next_y - self.y) * self.vel / kc) + self.y if self.vel < kc else self.next_y
        self.hitbox = (self.x, self.y, 200, 200)



    def draw(self,win):
        self.walkCount = self.walkCount + 1 if self.walkCount < 26 else 0
        if self.next_x > self.x:
            win.blit(self.hinhanhTrai[self.walkCount // 3], (self.x-25, self.y-25))
        else:
            win.blit(self.hinhanhPhai[self.walkCount // 3], (self.x-25, self.y-25))
        pygame.draw.rect(win, (255, 0,  0),(self.hitbox[0] - 14, self.hitbox[1] - 22, 50, 10))
        pygame.draw.rect(win, (0, 128, 0),
                         (self.hitbox[0] - 14, self.hitbox[1] - 22, 50 - (0.1 * (500 - self.health)), 10))

    def skill1(self, win, start_x, start_y, end_x, end_y):
        self.Q = 100
        self.skills.append(skill.Skill([pygame.image.load(r"picture/skill1.JPG-removebg-preview.png")], 10, start_x, start_y, end_x, end_y, 200, 1))


    def skill2(self, win, start_x, start_y, end_x, end_y):
        self.skills.append(skill.Skill([pygame.image.load(r"picture/skill2-removebg-preview.png")], 20, start_x, start_y, end_x, end_y, 200, 1))
        self.W = 150


    def ultimate(self, win, start_x, start_y, end_x, end_y):
        self.x = end_x
        self.y = end_y
        self.next_x = end_x
        self.next_y = end_y
        self.E = 500


    def attack(self, win, skill, start_x, start_y, end_x, end_y):
        if skill == "Q":
            self.skill1(win, start_x, start_y, end_x, end_y)
        elif skill == "W":
            self.skill2(win, start_x, start_y, end_x, end_y)
        elif skill == "E":
            self.ultimate(win, start_x, start_y, end_x, end_y)

    def hitted(self, enemyskill):
        self.health -= enemyskill.atk
        if self.health <= 0:
            self.tonTai = False




