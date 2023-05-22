import pygame

import calculator
import skill as skill
import player
import mimion
import enemy
import player
import skill
import tower
import mimion
import tru

pygame.init()

def ktraHitBox(a, b):
    if a.hitbox[0] <= b.hitbox[0] and a.hitbox[0] + a.hitbox[2] >= b.hitbox[0] \
            and a.hitbox[1] <= b.hitbox[1] and a.hitbox[1] + a.hitbox[3] >= b.hitbox[1]:
        return True
    return False



class GamePlay:

    def __init__(self):
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

        self.run = True
        self.run2 = True
        self.count = 0
        self.minionsPlayer = []
        self.minionsEnemy = []
        self.skills = []
        self.time = [0, 0, 0]
        self.tickcount = 0

    def settings(self):
        self.run = True
        self.change = False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.change = True
        return (self.run, self.change)

    def redrawWindow(self, change):

        self.win.blit(self.bg, (0, 0))

        #vẽ đạn từ trụ
        if self.redTurret.skills:
            self.redTurret.skills.draw(self.win, self.man)
        if self.blueTurret.skills:
            self.blueTurret.skills.draw(self.win, self.ene)

        #vẽ nhà chính và trụ
        self.redTurret.draw(self.win)
        self.blueTurret.draw(self.win)
        self.redTower.draw(self.win)
        self.blueTower.draw(self.win)

        for skill in self.ene.skills:
            skill.draw(self.win)

        for skill in self.man.skills:
            skill.draw(self.win)

        for minion in self.minionsPlayer:
            minion.draw(self.win)
        for minion in self.minionsEnemy:
            minion.draw(self.win)

        self.man.draw(self.win)
        self.ene.draw(self.win)

        pygame.display.update()

    def turretAttack(self):

        self.redTurret.attack(self.man, self.minionsPlayer)
        self.blueTurret.attack(self.ene, self.minionsEnemy)
    def playMove(self):

        self.man.move(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.change)
        self.ene.move(self.man, self.time[0] * 60 + self.time[1])

        for minion in self.minionsPlayer:
            minion.move(self.ene, self.minionsEnemy)

        for minion in self.minionsEnemy:
            minion.move(self.man, self.minionsPlayer)

    def playerAttack(self):
        keys = pygame.key.get_pressed()
        # giam thoi gian hoi chieu cua ba chieu

        self.man.Q = 0 if self.man.Q <= 0 else self.man.Q - 1
        self.man.W = 0 if self.man.W <= 0 else self.man.W - 1
        self.man.E = 0 if self.man.E <= 0 else self.man.E - 1

        # tan cong neu nut chieu duoc an va thoi gian hoi chieu bang 0
        if keys[pygame.K_e] and self.man.E == 0:
            self.man.attack(self.win, "E", self.man.x, self.man.y, pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10)
        elif keys[pygame.K_w] and self.man.W == 0:
            self.man.attack(self.win, "W", self.man.x, self.man.y, pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10)
        elif keys[pygame.K_q] and self.man.Q == 0:
            self.man.attack(self.win, "Q", self.man.x, self.man.y, pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10)

    def enemyAttack(self):

        self.ene.Q = 0 if self.ene.Q <= 0 else self.ene.Q - 1
        self.ene.W = 0 if self.ene.W <= 0 else self.ene.W - 1
        self.ene.E = 0 if self.ene.E <= 0 else self.ene.E - 1

        kc = calculator.khoangCach(self.ene.x, self.ene.y, self.man.x, self.man.y)

        if kc < 100 and self.ene.E == 0:
            self.ene.attack(self.win, "E", self.ene.x, self.ene.y, self.man.x + 10, self.man.y + 10)
        elif kc < 200 and self.ene.W == 0:
            self.ene.attack(self.win, "W", self.ene.x, self.ene.y, self.man.x + 10, self.man.y + 10)
        elif kc < 100 and self.ene.Q == 0:
            self.ene.attack(self.win, "Q", self.ene.x, self.ene.y, self.man.x + 10, self.man.y + 10)

    def playEvent(self):

        if (self.time[0] * 60 + self.time[1]) % 10 == 0 and self.time[2] == 0:
            self.minionsEnemy.append(mimion.Minion(False, 1239, 153))
            self.minionsPlayer.append((mimion.Minion(True, 152, 623)))

        self.playMove()

        for sk in self.ene.skills:
            if ktraHitBox(sk, self.man):
                self.man.hitted(sk)

        for minion in self.minionsPlayer:
            minion.skills.append(
                skill.Skill(pygame.image.load(r"picture/bullet.png"), 5, minion.x, minion.y, self.ene.x, self.ene.y, 10, 1))
            for sk in minion.skills:
                if ktraHitBox(sk, self.ene):
                    self.ene.hitted(sk)

        for minion in self.minionsEnemy:
            minion.skills.append(
                skill.Skill(pygame.image.load(r"picture/bullet.png"), 5, minion.x, minion.y, self.ene.x, self.ene.y, 10, 1))
            for sk in minion.skills:
                if ktraHitBox(sk, self.man):
                    self.man.hitted(sk)

        for red in self.minionsPlayer:
            for blue in self.minionsEnemy:
                if ktraHitBox(red, blue):
                    red.hitted(blue.skill[0])
                    blue.hitted(red.skill[0])

        for sk in self.man.skills:
            if ktraHitBox(sk, self.ene) or ktraHitBox(self.ene, sk):
                self.ene.hitted(sk)


        self.minionsPlayer = list(filter(lambda x: x.tonTai, self.minionsPlayer[:]))  # Loc cac doi tuong linh con song
        self.minionsEnemy = list(filter(lambda x: x.tonTai, self.minionsEnemy[:]))  # Loc cac doi thuong linh con song
        self.ene.skills = list(filter(lambda x: x.tonTai, self.ene.skills[:]))
        self.man.skills = list(filter(lambda x: x.tonTai, self.man.skills[:]))
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

            self.playEvent()

            self.redrawWindow(self.change)

            self.time[2] += 1

        pygame.quit()

