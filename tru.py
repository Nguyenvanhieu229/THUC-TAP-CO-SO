import pygame.image


class Turret:
    def __init__(self, img, x, y):
        self.health = 1000
        self.img = img
        self.tancong = 100
        self.thu = 30
        self.hitbox = (1, 1)
        self.hinhanh = []
        self.x = x
        self.y = y
        self.tonTai = True
        self.range = 100;

    def draw(self,win):
        #se dung im tai cho


        pygame.draw.ellipse(win, color="green", rect=(self.x - 70, self.y + 50, 240, 170), width=2)
        win.blit(self.img, (self.x, self.y))


    #def tanCong(self):
        #tan cong neu co doi tuong trong pham vi


    def hitted(self, enemyskill):
        self.mau -= enemyskill.atk
        #am thanh
        if self.mau <= 0:
            self.tonTai = False
            #game ket thuc