import pygame

import calculator
import skill
import player
import minion as mn
import enemy
import player
import tower
import minion
import tru


def ktraHitBox(a, b):

    if a == None or b == None:
        return False

    if a.hitbox[0] <= b.hitbox[0] and a.hitbox[0] + a.hitbox[2] >= b.hitbox[0] \
            and a.hitbox[1] <= b.hitbox[1] and a.hitbox[1] + a.hitbox[3] >= b.hitbox[1]:
        return True
    if b.hitbox[0] <= a.hitbox[0] and b.hitbox[0] + b.hitbox[2] >= a.hitbox[0] \
            and b.hitbox[1] <= a.hitbox[1] and b.hitbox[1] + b.hitbox[3] >= a.hitbox[1]:
        return True

    return False



class GamePlay:

    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((1366, 768))
        self.bg = pygame.image.load(r"picture/bacg.png")
        self.clock = pygame.time.Clock()
        self.clock2 = pygame.time.Clock()
        self.man = player.Player()
        self.ene = enemy.Enemy()
        self.redTurret = tru.Turret(pygame.image.load(r"picture/truDo.png"), 1008, 125)
        self.blueTurret = tru.Turret(pygame.image.load(r"picture/truXanh.png"), 330, 470)
        self.reset = 0
        self.redTower = tower.Tower(pygame.image.load(r"picture/nhaDo.png"), 1190, 0)
        self.blueTower = tower.Tower(pygame.image.load(r"picture/nhaXanh.png"), 10, 600)
        self.thoiGianHoiSinh = 300
        self.thoiGianHoiSinhQuai = 300
        self.kda = [0,0,0]
        self.font2 = pygame.font.SysFont("comicsans", 20, True)
        self.run = True
        self.run2 = True
        self.count = 0
        self.minionsPlayer = []
        self.minionsEnemy = []
        self.skills = []
        self.time = [0, 0, 0]
        self.tickcount = 0
        self.font1 = pygame.font.SysFont("comicsans", 50, True)
        self.skillInfo = pygame.image.load(r"picture/ava.png")
        self.avatar = pygame.image.load(r"picture/avatar.png")
        self.v1 = pygame.image.load(r"picture/v1.png")
        self.v2 = pygame.image.load(r"picture/v2.png")
        self.vs = pygame.image.load(r"picture/vs.png")
        self.deadAllyMini = 0
        self.deadEneMini=0


    def settings(self):
        self.run = True
        self.change = False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.change = True
        if self.redTower.tonTai == False:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run = False

            #nguoi choi cvasfafadfed.
        elif self.blueTower.tonTai == False:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.run = False
            #nguoi choi thua

        return (self.run, self.change)

    def redrawWindow(self, change):
        #HIeu thu
        # ve nen
        self.win.blit(self.bg, (0, 0))
        obj = self.checkMouse(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        if not obj and change:
            self.win.blit(pygame.image.load(r"picture/foot.png"),(self.man.next_x,self.man.next_y))
        #ve thoi gian
        text = self.font2.render("Time: " + str(self.time[0]) + ":" + str(self.time[1]), 1, (0, 0, 0))
        pygame.draw.rect(self.win, (0,255,255), (0,0,120,30))
        self.win.blit(text, (0, 0))

        #ve kda
        text = self.font2.render("K: " + str(self.kda[0]) + "   D: " + str(self.kda[1]) + "   EXP: " + str(self.man.exp) + "/" + str(self.man.maxExp), 1, (0, 0, 0))
        pygame.draw.rect(self.win, (0, 255, 255), (600, 0, 200, 30))
        self.win.blit(text, (600,0))
        # vẽ đạn từ trụ
        for sk in self.redTurret.skills:
            sk.draw(self.win)

        for sk in self.blueTurret.skills:
            sk.draw(self.win)

        # vẽ nhà chính và trụ
        self.redTurret.draw(self.win)
        self.blueTurret.draw(self.win)
        self.redTower.draw(self.win)
        self.blueTower.draw(self.win)

        # ve skill cua nhan vat va may
        for skill in self.ene.skills:
            skill.draw(self.win)

        for skill in self.man.skills:
            skill.draw(self.win)

        # ve linh hai ben
        for minion in self.minionsPlayer:
            minion.draw(self.win)
            for sk in minion.skills:
                sk.draw(self.win)


        for minion in self.minionsEnemy:
            minion.draw(self.win)
            for sk in minion.skills:
                sk.draw(self.win)

        # ve nhan vat nguoi va may
        self.man.draw(self.win)
        self.ene.draw(self.win)

        if self.man.health <= 0 :
            text1 = self.font1.render("Revive in " + str(int(self.thoiGianHoiSinh/30)) + " seconds", 1, (0, 0, 0))
            self.win.blit(text1,(500,300))

        if self.redTower.health <= 0:
            text1 = self.font1.render("VICTORY", 1, (0, 0, 0))
            self.win.blit(text1, (500, 300))
            text2 = self.font2.render("REMATCH",1,(0,0,0))
            self.win.blit(text2,(550,400))

        elif self.blueTower.health <= 0:
            text1 = self.font1.render("DEFEATED", 1, (0, 0, 0))
            self.win.blit(text1, (500, 300))
            text2 = self.font2.render("REMATCH", 1, (0, 0, 0))
            self.win.blit(text2, (550, 400))
        self.drawSkillInfor()
        self.win.blit(self.v1, (1100, 550))
        self.win.blit(self.v2,(1100,670))
        self.drawHoiSinh()
        pygame.display.update()

    def turretAttack(self):
        '''
            Tru tan cong linh va nguoi choi
            :return: void
        '''
        self.redTurret.attack(self.man, self.minionsPlayer)
        self.blueTurret.attack(self.ene, self.minionsEnemy)

    def playMove(self):

        # nhan vat do nguoi choi va may di chuyen
        if self.man.health > 0:
            self.man.move(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.change)

        if self.ene.health > 0:
            self.ene.move(self.man, self.time[1], self.minionsPlayer, self.blueTurret, self.blueTower)

        # linh di chuyen
        for minion in self.minionsPlayer:
            minion.move(self.ene, self.minionsEnemy, self.redTurret)

        for minion in self.minionsEnemy:
            minion.move(self.man, self.minionsPlayer, self.blueTurret)


    def playerAttack(self):
        keys = pygame.key.get_pressed()
        # giam thoi gian hoi chieu cua ba chieu

        self.man.Q = 0 if self.man.Q <= 0 else self.man.Q - 1
        self.man.W = 0 if self.man.W <= 0 else self.man.W - 1
        self.man.E = 0 if self.man.E <= 0 else self.man.E - 1
        self.man.A = 0 if self.man.A <= 0 else self.man.A - 1

        # tan cong neu nut chieu duoc an va thoi gian hoi chieu bang 0
        if keys[pygame.K_e] and self.man.E == 0:
            self.man.attack(self.win, "E", self.man.x, self.man.y, pygame.mouse.get_pos()[0] - 85, pygame.mouse.get_pos()[1] - 110)
        elif keys[pygame.K_w] and self.man.W == 0:
            self.man.attack(self.win, "W", self.man.x, self.man.y, pygame.mouse.get_pos()[0] + 12, pygame.mouse.get_pos()[1] + 12)
        elif keys[pygame.K_q] and self.man.Q == 0:
            self.man.attack(self.win, "Q", self.man.x, self.man.y, pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10)
        elif keys[pygame.K_a] and self.man.A == 0:
            target = self.checkMouse(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
            if target and calculator.khoangCach(self.man.x,self.man.y,target.x,target.y) <= self.man.range:
                self.man.danhThuong(target)

    def enemyAttack(self):

        self.ene.Q = 0 if self.ene.Q <= 0 else self.ene.Q - 1
        self.ene.W = 0 if self.ene.W <= 0 else self.ene.W - 1
        self.ene.E = 0 if self.ene.E <= 0 else self.ene.E - 1
        self.ene.A = 0 if self.ene.A <= 0 else self.ene.A - 1

        kc = calculator.khoangCach(self.ene.x, self.ene.y, self.man.x, self.man.y)

        if kc < 100 and self.ene.E == 0:
            self.ene.attack(self.win, "E", self.ene.x, self.ene.y, self.man.x - 30, self.man.y - 30)
        elif kc < 200 and self.ene.W == 0:
            self.ene.attack(self.win, "W", self.ene.x, self.ene.y, self.man.x + 10, self.man.y + 10)
        elif kc < 100 and self.ene.Q == 0:
            self.ene.attack(self.win, "Q", self.ene.x, self.ene.y, self.man.x + 10, self.man.y + 10)
        elif self.ene.A == 0:
            self.ene.danhThuong(self.man, self.minionsPlayer, self.blueTurret, self.blueTower)

    def playEvent(self):
        if self.checkMouse(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) \
                and self.checkMouse(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]).health > 0:
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        # sinh linh
        if (self.time[0] * 60 + self.time[1]) % 10 == 0 and self.time[2] == 0:
            self.minionsEnemy.append(mn.Minion(False, 1239, 153))
            self.minionsPlayer.append((mn.Minion(True, 152, 623)))

        if self.man.health <= 0:

            if self.thoiGianHoiSinh == 300:
                self.kda[1] = self.kda[1] + 1

            self.thoiGianHoiSinh= self.thoiGianHoiSinh - 1

            if self.thoiGianHoiSinh == 0:
                self.man = player.Player()
                self.thoiGianHoiSinh = 300

        if self.ene.health <= 0:
            if self.thoiGianHoiSinhQuai == 300:
                self.kda[0] = self.kda[0] + 1

            self.thoiGianHoiSinhQuai= self.thoiGianHoiSinhQuai - 1
            if self.thoiGianHoiSinhQuai == 0:

                self.ene = enemy.Enemy()
                self.thoiGianHoiSinhQuai = 300

        # upgrade player
        if self.deadEneMini > 0 :
            self.man.exp += 100*self.deadEneMini
            if self.man.exp >= self.man.maxExp:
                if self.man.lv < 9:
                    self.man.lv += 1
                    self.man.maxExp += self.man.lv*100


        # update enemy
        if self.deadAllyMini > 0:
            self.ene.exp += 100*self.deadAllyMini
            if self.ene.exp >= self.ene.maxExp:
                if self.ene.lv < 9:
                    self.ene.lv += 1
                    self.ene.maxExp += self.ene.lv*100


        # thuc hien cac viec di chuyen
        self.playMove()

        # nguoi bi danh boi may
        for sk in self.ene.skills:
            if ktraHitBox(sk, self.man):
                self.man.hitted(sk)

        # nguoi bi danh boi linh
        for minion in self.minionsEnemy:
            for sk in minion.skills:
                if ktraHitBox(sk, self.man):
                    self.man.hitted(sk)

        # nguoi bi danh boi tru
        for sk in self.redTurret.skills:
            if ktraHitBox(sk, self.man):
                self.man.hitted(sk)

        # may bi danh boi nguoi
        for sk in self.man.skills:
            if ktraHitBox(sk, self.ene):
                self.ene.hitted(sk)


        # may bi danh boi linh
        for minion in self.minionsPlayer:
            for sk in minion.skills:
                if ktraHitBox(sk, self.ene):
                    self.ene.hitted(sk)

        # may bi danh boi tru
        for sk in self.blueTurret.skills:
            if ktraHitBox(sk, self.ene):
                self.ene.hitted(sk)

        # linh bi danh boi tru
        for blue in self.minionsPlayer:
            for sk in self.redTurret.skills:
                if ktraHitBox(blue, sk):
                    blue.hitted(sk)

        for red in self.minionsEnemy:
            for sk in self.blueTurret.skills:
                if ktraHitBox(red, sk):
                    red.hitted(sk)

        # linh bi danh boi nguoi
        for blue in self.minionsPlayer:
            for sk in self.ene.skills:
                if ktraHitBox(blue, sk):
                    blue.hitted(sk)

        for red in self.minionsEnemy:
            for sk in self.man.skills:
                if ktraHitBox(red, sk):
                    red.hitted(sk)

        # linh bi danh boi linh
        for blue in self.minionsPlayer:
            for red in self.minionsEnemy:
                for sk in red.skills:
                    if ktraHitBox(blue, sk):
                        blue.hitted(sk)

        for red in self.minionsEnemy:
            for blue in self.minionsPlayer:
                for sk in blue.skills:
                    if ktraHitBox(sk, red):
                        red.hitted(sk)

        # tru bi danh boi nhan vat
        for sk in self.man.skills:
            if ktraHitBox(self.redTurret, sk):
                self.redTurret.hitted(sk)

        for sk in self.ene.skills:
            if ktraHitBox(self.blueTurret, sk):
                self.blueTurret.hitted(sk)

        # tru bi danh boi linh
        for blue in self.minionsPlayer:
            for sk in blue.skills:
                if ktraHitBox(sk, self.redTurret):
                    self.redTurret.hitted(sk)

        for red in self.minionsEnemy:
            for sk in red.skills:
                if ktraHitBox(sk, self.blueTurret):
                    self.blueTurret.hitted(sk)

        # nha bi danh boi nhan vat
        for sk in self.man.skills:
            if ktraHitBox(self.redTower, sk):
                self.redTower.hitted(sk, self.redTurret)

        for sk in self.ene.skills:
            if ktraHitBox(self.blueTower, sk):
                self.blueTower.hitted(sk, self.blueTurret)

        # nha bi danh boi linh
        for blue in self.minionsPlayer:
            for sk in blue.skills:
                if ktraHitBox(sk, self.redTower):
                    self.redTower.hitted(sk, self.redTurret)

        for red in self.minionsEnemy:
            for sk in red.skills:
                if ktraHitBox(sk, self.blueTower):
                    self.blueTower.hitted(sk, self.blueTurret)

        self.deadAllyMini = len(list(filter(lambda x: not x.tonTai, self.minionsPlayer[:])))
        self.minionsPlayer = list(filter(lambda x: x.tonTai, self.minionsPlayer[:])) #Loc cac doi tuong linh con song
        self.deadEneMini = len(list(filter(lambda x: not x.tonTai, self.minionsEnemy[:])))
        self.minionsEnemy = list(filter(lambda x: x.tonTai, self.minionsEnemy[:]))  #Loc cac doi thuong linh con song
        self.ene.skills = list(filter(lambda x: x.tonTai > 0, self.ene.skills[:]))
        self.man.skills = list(filter(lambda x: x.tonTai > 0, self.man.skills[:]))
        self.redTurret.skills = list(filter(lambda x: x.tonTai > 0, self.redTurret.skills[:]))
        self.blueTurret.skills = list(filter(lambda x: x.tonTai > 0, self.blueTurret.skills[:]))

        for blue in self.minionsPlayer:
            blue.skills = list(filter(lambda x: x.tonTai > 0, blue.skills[:]))

        for blue in self.minionsEnemy:
            blue.skills = list(filter(lambda x: x.tonTai > 0, blue.skills[:]))



    def minionsAttack(self):

        for blue in self.minionsPlayer:
            blue.attack(self.ene, self.minionsEnemy, self.redTurret, self.redTower)

        for red in self.minionsEnemy:
            red.attack(self.man, self.minionsPlayer, self.blueTurret, self.blueTower)

    def play(self):

        while self.run:
            self.clock.tick(30)
            if self.time[2] == 30:
                self.time[1] += 1
                self.time[2] = 0
            if self.time[1] == 60:
                self.time[0] += 1
                self.time[1] = 0

            self.change = False
            self.run, self.change = self.settings()

            self.playerAttack()
            self.enemyAttack()
            self.turretAttack()
            self.minionsAttack()

            self.playEvent()

            self.redrawWindow(self.change)

            self.time[2] += 1

        pygame.quit()

    def checkMouse(self,x1,y1):
        for minion in self.minionsEnemy:
            if minion.x < x1 and x1 < minion.x + 50 and minion.y < y1 and y1 < minion.y+ 50:
                return minion

        if self.redTurret.x < x1 and x1 < self.redTurret.x + 50 and self.redTurret.y < y1 and y1 < self.redTurret.y + 100:
                return self.redTurret

        if self.redTower.x < x1 + 50 and x1 < self.redTower.x + 100 and self.redTower.y < y1 + 50 and y1 < self.redTower.y + 100 and self.redTurret.health <= 0:
                return self.redTower

        if self.ene.x < x1 and x1 < self.ene.x + 50 and self.ene.y < y1 and y1 < self.ene.y + 50:
                return  self.ene


    def drawSkillInfor(self):
        self.win.blit(self.skillInfo, (580, 700))
        self.win.blit(self.avatar, (568, 700))
        q = self.man.Q/30
        if q != 0:
            text1 = self.font1.render(str(int(q)), 1, (240, 248, 255))
            self.win.blit(text1, (674, 703))
        w = self.man.W/ 30
        if w != 0:
            text1 = self.font1.render(str(int(w)), 1, (240, 248, 255))
            self.win.blit(text1, (750, 703))
        e = self.man.E / 30
        if e != 0:
            text1 = self.font1.render(str(int(e)), 1, (240, 248, 255))
            self.win.blit(text1, (826, 703))

    def drawHoiSinh(self):
        if self.man.health <= 0:
            p1 = self.thoiGianHoiSinh/30
            if p1!=0:
                text1 = self.font1.render(str(int(p1)), 1, (240, 248, 255))
                self.win.blit(text1, (1300, 570))
        if self.ene.health <= 0:
            p2 = self.thoiGianHoiSinhQuai/30
            if p2!=0:
                text1 = self.font1.render(str(int(p2)), 1, (240, 248, 255))
                self.win.blit(text1, (1150, 680))
        pygame.draw.line(self.win,(240, 248, 255),(1101,671),(1366,671))
        self.win.blit(self.vs, (1185, 630))








