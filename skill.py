import pygame
import calculator

class Skill:
    def __init__(self, img, atk, start_x, start_y, end_x, end_y, range, soAnh):
        self.img = img
        self.atk = atk
        self.range = range
        self.start_x = start_x
        self.start_y = start_y
        self.walkCount = 0
        self.vel = 6
        self.tonTai = 1
        self.hitbox = (start_x - 2,start_y - 2, 10, 10)
        self.soAnh = soAnh
        kc = calculator.khoangCach(start_x, start_y, end_x, end_y)
        self.end_x = int((end_x - self.start_x) * self.range / kc) + self.start_x if end_x != start_x else end_x
        self.end_y = int((end_y - self.start_y) * self.range / kc) + self.start_y if end_y != start_y else end_y



    def draw(self, win):
        if self.walkCount < self.soAnh - 1:
            self.walkCount += 1
        else:
            self.walkCount = 0
        kc = calculator.khoangCach(self.start_x, self.start_y, self.end_x, self.end_y)

        if kc == 0:
            self.tonTai = 0

        if self.tonTai > 0:
            win.blit(self.img[self.walkCount], (self.start_x, self.start_y))
        self.start_x = ((self.end_x - self.start_x) * self.vel / kc) + self.start_x if (self.vel < kc and kc != 0) else self.end_x
        self.start_y = ((self.end_y - self.start_y) * self.vel / kc) + self.start_y if (self.vel < kc and kc != 0) else self.end_y
        self.hitbox = (self.start_x - 2, self.start_y - 2, 20, 20)
