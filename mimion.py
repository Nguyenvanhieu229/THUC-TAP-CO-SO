import pygame.image

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
        self.health = 100
        self.range = 200
        self.walkCount = 0
        self.skills = []
        self.health = 10
        self.x = x
        self.y = y
        self.tonTai = True
        self.hitbox = (self.x, self.y, 30, 30)
        self.ben = ben
        self.vel = 2
        self.cho = 0
        self.next_x = 1239 if ben else 153
        self.next_y = 151 if ben else 623

    def draw(self, win):

        if self.walkCount == 15:
            self.walkCount = 0

        if self.ben:
            win.blit(self.img2[self.walkCount//5], (self.x, self.y))
        else:
            win.blit(self.img[self.walkCount // 5], (self.x, self.y))
        self.walkCount += 1
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 5, self.hitbox[1] - 22, 50, 10))
        pygame.draw.rect(win, (0, 128, 0),
                         (self.hitbox[0] - 5, self.hitbox[1] - 22, 50 - (0.1 * (500 - self.health)), 10))

    def move(self, ene, minions):
        minx, miny = calculator.find(self, ene, minions)
        kcDich = calculator.khoangCach(self.x, self.y, minx, miny)
        kc = calculator.khoangCach(self.x, self.y, self.next_x, self.next_y)

        if kcDich > self.range:
            self.x = ((self.next_x - self.x) * self.vel / kc) + self.x if self.vel < kc else self.x
            self.y = ((self.next_y - self.y) * self.vel / kc) + self.y if self.vel < kc else self.y

        self.hitbox = (self.x, self.y, 20, 20)

    def attack(self, end_x, end_y):
        self.cho = 30
        self.skills.append(not_move_skill.NotMoveSkill([pygame.image.load(r"picture/skill1.JPG-removebg-preview.png")],
                                                       5, end_x, end_y, 100, 1, 1))
        if len(self.skills) > 1:
            self.skills.pop(0)

    def hitted(self, enemyskill):

        self.health -= enemyskill.atk
        enemyskill.tonTai = False

        if self.health <= 0:
            self.tonTai = False