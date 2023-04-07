import pygame.draw


class Tower:
    def __int__(self):
        self.health = 1000
        self.range = 300
        #self.hinhanh =
        self.x = 100
        self.y = 100
        self.tonTai = True

    def draw(self, win):
        #win.blit(self.img, (self.x, self.y))
        pygame.draw.circle(surface=win, center=(20, 20), radius=self.range, width=2)


    def biDanhTrung(self, chiSo):
        self.mau -= chiSo
        #am thanh
        if self.mau <= 0:
            self.tonTai = False
            #game ket thuc