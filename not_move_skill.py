import skill

class NotMoveSkill(skill.Skill):
    def __init__(self, img, atk, start_x, start_y, range, soAnh, tonTai):
        super().__init__(img, atk, start_x, start_y, start_x, start_y, range, soAnh)
        self.tonTai = tonTai
        self.vel = 0

    def draw(self, win):
        if self.walkCount < self.soAnh - 1:
            self.walkCount += 1
        else:
            self.walkCount = 0
        if self.tonTai > 0:
            win.blit(self.img[self.walkCount], (self.start_x, self.start_y))
        self.tonTai -= 1


