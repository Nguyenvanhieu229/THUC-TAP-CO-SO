class Nha:
    def __int__(self):
        self.health = 1000
        self.tancong = 10
        self.thu = 30
        self.hitbox = (1, 1)
        self.hinhanh = []
        self.x = 100#toa do
        self.y = 100
        self.tonTai = True
        self.phamVi = 200;

    def draw(self):
        #se dung im tai cho

    def tanCong(self):
        #tan cong neu co doi tuong trong pham vi


    def biDanhTrung(self, chiSo):
        self.mau -= chiSo
        #am thanh
        if self.mau <= 0:
            self.tonTai = False
            #game ket thuc