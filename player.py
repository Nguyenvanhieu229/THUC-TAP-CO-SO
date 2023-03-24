import pygame
import math
import tinhToan



class Player:
    def __init__(self):
        self.next_x = 0
        self.next_y = 0
        self.mau = 1000
        self.tancong = 50
        self.walkCount = 0
        self.thu = 20
        self.nangluong = 100
        self.hinhanhTrai = [pygame.image.load(r'picture\main character\R1.png'), pygame.image.load(r'picture\main character\R2.png'), pygame.image.load(r'picture\main character\R3.png'), pygame.image.load(r'picture\main character\R4.png'), pygame.image.load(r'picture\main character\R5.png'), pygame.image.load(r'picture\main character\R6.png'),pygame.image.load(r'picture\main character\R7.png'), pygame.image.load(r'picture\main character\R8.png'), pygame.image.load(r'picture\main character\R9.png')]
        self.hinhanhPhai = [pygame.image.load(r'picture\main character\L1.png'), pygame.image.load(r'picture\main character\L2.png'), pygame.image.load(r'picture\main character\L3.png'), pygame.image.load(r'picture\main character\L4.png'), pygame.image.load(r'picture\main character\L5.png'), pygame.image.load(r'picture\main character\L6.png'), pygame.image.load(r'picture\main character\L7.png'), pygame.image.load(r'picture\main character\L8.png'), pygame.image.load(r'picture\main character\L9.png')]
        self.vel = 5
        self.Q = 0
        self.W = 0
        self.E = 0
        self.x = 100
        self.y = 100
        self.tonTai = True

    def draw(self, win, next_x, next_y, move):
        # print(next_x, next_y)
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if move:
            self.next_x = next_x
            self.next_y = next_y
        if self.vel >= math.sqrt((self.x - self.next_x) **2 + (self.y - self.next_y) **2):
            self.x = self.next_x
            self.y = self.next_y
        else:
            self.x = (self.vel * (self.next_x - self.x))/math.sqrt((self.x - self.next_x) **2 + (self.y - self.next_y) **2) + self.x
            self.y = (self.vel * (self.next_y - self.y))/math.sqrt((self.x - self.next_x) **2 + (self.y - self.next_y) **2) + self.y
        if self.x <= self.next_x:
            win.blit(self.hinhanhTrai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.hinhanhPhai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def skill1(self, win):
        print('skill1')
        self.Q = 300


    def skill2(self, win):
        print("skill2")
        self.W = 300

    def ultilmate(self, win):
        print("ultilmate")
        self.E = 300

    def attack(self, win, skill):
        if skill == "Q":
            self.skill1(win)
        elif skill == "W":
            self.skill2(win)
        elif skill == "E":
            self.ultilmate(win)