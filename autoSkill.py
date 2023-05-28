
import skill
import calculator

class AutoSkill(skill.Skill):

    def __init__(self, img, atk, start_x, start_y, mucTieu, range, soAnh):
        super().__init__(img, atk, start_x, start_y, mucTieu.x, mucTieu.y, range, soAnh)
        self.mucTieu = mucTieu
        self.vel = 8

    def draw(self, win):

        # neu muc tieu da chet hoac chieu da het han ton tai thi khong ve nua
        if self.mucTieu.health == 0 or self.tonTai == 0:
            self.tonTai = 0
            return

        self.end_x = self.mucTieu.x
        self.end_y = self.mucTieu.y

        if self.walkCount < self.soAnh - 1:
            self.walkCount += 1
        else:
            self.walkCount = 0

        kc = calculator.khoangCach(self.start_x, self.start_y, self.end_x, self.end_y)
        if self.tonTai:
            win.blit(self.img[self.walkCount], (self.start_x, self.start_y))

        self.start_x = ((self.end_x - self.start_x) * self.vel / kc) + self.start_x if (self.vel < kc and kc != 0) else self.end_x
        self.start_y = ((self.end_y - self.start_y) * self.vel / kc) + self.start_y if (self.vel < kc and kc != 0) else self.end_y
        self.hitbox = (self.start_x - 2, self.start_y - 2, 20, 20)


