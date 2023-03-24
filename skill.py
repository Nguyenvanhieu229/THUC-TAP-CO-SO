import pygame
import tinhToan

class Skill:
    def __init__(self, img, atk, start_x, start_y, end_x, end_y, range):
        self.img = img
        self.atk = atk
        self.range = range
        self.start_x = start_x
        self.start_y = start_y
        self.vel = 10
        kc = tinhToan.khoangCach(start_x, start_y, end_x, end_y)
        self.end_x = int((end_x - self.start_x) * self.range / kc) + self.start_x
        self.end_y = int((end_y - self.start_y) * self.range / kc) + self.start_y



    def draw(self, win):
        kc = tinhToan.khoangCach(self.start_x, self.start_y, self.end_x, self.end_y)
        win.blit(self.img, (self.start_x, self.start_y))
        self.start_x = int((self.end_x - self.start_x) * self.vel / kc) + self.start_x if self.vel < kc else self.end_x
        self.start_y = int((self.end_y - self.start_y) * self.vel / kc) + self.start_y if self.vel < kc else self.end_y

