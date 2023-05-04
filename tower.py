import pygame.draw


class Tower:
    def __init__(self, img, x, y):
        self.health = 1000
        self.range = 300
        self.img = img
        #self.hinhanh =
        self.x = x
        self.y = y
        self.tonTai = True

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))



    def biDanhTrung(self, chiSo):
        self.mau -= chiSo
        #am thanh
        if self.mau <= 0:
            self.tonTai = False
            #game ket thuc