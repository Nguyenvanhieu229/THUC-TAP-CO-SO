import pygame.image

class Minion:
    def __init__(self, ben, x):
        self.img = pygame.image.load(r"picture\enemy\L1E.png")
        self.mau = 100
        self.tancong = 5
        self.thu = 10
        self.x = x
        self.y = 250
        self.tonTai = True
        self.hitbox = (1,1)
        self.ben = ben
        self.vel = 3

    def draw(self, win):
        if self.ben:
            phia = 1
        else:
            phia = -1
        self.x += self.vel * phia
        win.blit(self.img, (self.x+1, self.y))

    def biDanhTrung(self, chiSo):
        self.mau -= chiSo
        #am thanh
        if self.mau <= 0:
            self.tonTai = False