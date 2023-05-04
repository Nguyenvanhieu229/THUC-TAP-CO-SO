import pygame
import calculator
import math
import random
import player
import skill


class Enemy:
    def __init__(self):
        self.next_x = 0
        self.next_y = 0
        self.health = 500
        self.tancong = 50
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
        self.x = 100
        self.y = 100
        self.hitbox = (self.x, self.y, 50, 50)
        self.tonTai = True

    def move(self, man, reset):
        if reset % 2 == 0:
            self.next_x, self.next_y = random.randint(man.x - 20, man.x+20), random.randint(man.y-20, man.y+20)

        #minx, miny = tinhToan.find(self, man, minionPlayer)
        kc = calculator.khoangCach(self.x, self.y, self.next_x, self.next_y)
        if kc > self.range:
            self.x = int((self.next_x - self.x) * self.vel / kc) + self.x if self.vel < kc else self.next_x
            self.y = int((self.next_y - self.y) * self.vel / kc) + self.y if self.vel < kc else self.next_y

        self.hitbox = (self.x, self.y, 50, 50)

    def draw(self, win):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.x >= self.next_x:
            win.blit(self.hinhanhTrai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.hinhanhPhai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 10, self.hitbox[1] - 10, 50, 10))
        pygame.draw.rect(win, (0, 128, 0),
                         (self.hitbox[0] + 10, self.hitbox[1] - 10, 50 - (0.1 * (500 - self.health)), 10))



    def hitted(self, sk):
        self.health -= sk.atk
        sk.tonTai = False
        if self.health <= 0:
            self.tonTai = False

    def skill1(self, win, start_x, start_y, end_x, end_y):
        self.Q = 0
        self.skills.append(skill.Skill([pygame.image.load(r"picture/main character/skills/skill1.png")], 10, start_x, start_y, end_x, end_y, 200, 1))


    def skill2(self, win, start_x, start_y, end_x, end_y):
        self.skills.append(skill.Skill([pygame.image.load(r"picture/main character/skills/skill2.png"), pygame.image.load(r"picture/main character/skills/skill2.png"),
                                        pygame.image.load(r"picture/main character/skills/skill2.png"), pygame.image.load(r"picture/main character/skills/skill2.png"),
                                       pygame.image.load(r"picture/main character/skills/skill2.png"), pygame.image.load(r"picture/main character/skills/skill2.png")], 20, start_x, start_y, end_x,
                        end_y, 200, 6))
        self.W = 0


    def ultimate(self, win, start_x, start_y, end_x, end_y):
        self.skills.append(skill.Skill([pygame.image.load(r"picture/main character/skills/util.png")], 30, end_x, end_y, end_x, end_y, 300, 1))
        self.E = 0

    def attack(self, win, skill, start_x, start_y, end_x, end_y):
        if skill == "Q":
            self.skill1(win, start_x, start_y, end_x, end_y)
        elif skill == "W":
            self.skill2(win, start_x, start_y, end_x, end_y)
        elif skill == "E":
            self.ultimate(win, start_x, start_y, end_x, end_y)