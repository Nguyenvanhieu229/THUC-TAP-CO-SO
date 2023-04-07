import pygame
import tinhToan

class Enemy:
    def __init__(self):
        self.next_x = 0
        self.next_y = 0
        self.health = 1000
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
        self.tonTai = True

    def draw(self, win, man, minionPlayer):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        minx, miny = tinhToan.find(self, man, minionPlayer)
        kc = tinhToan.khoangCach(self.x, self.y, minx, miny)
        if kc > self.range:
            self.x = int((minx - self.x) * self.vel / kc) + self.x if self.vel < kc else minx
            self.y = int((miny - self.y) * self.vel / kc) + self.y if self.vel < kc else miny
        if self.x >= minx:
            win.blit(self.hinhanhTrai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.hinhanhPhai[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    # def tanCong(self, loai):
    #     #ramdom de chon loai tan cong

    def biDanhTrung(self, chiSo):
        self.mau -= chiSo
        #am thanh
        if self.mau <= 0:
            self.tonTai = False