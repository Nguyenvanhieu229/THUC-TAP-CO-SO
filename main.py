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



win = pygame.display.set_mode((1366, 768))
bg = pygame.image.load(r"picture/bacg.png")
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
man = player.Player()
ene = enemy.Enemy()
redTurret = tru.Turret(pygame.image.load(r"picture/truDo.png"), 1008, 125)
blueTurret = tru.Turret(pygame.image.load(r"picture/truXanh.png"), 330, 470)
reset = 0
redTower = tower.Tower(pygame.image.load(r"picture/nhaDo.png"), 1190, 0)
blueTower = tower.Tower(pygame.image.load(r"picture/nhaXanh.png"), 10, 600)



run = True
run2= True
count = 0
minionsPlayer = []
minionsEnemy = []
skills = []
time = [0, 0, 0]
tickcount = 0



def redrawWindow(change):

    win.blit(bg, (0, 0))

    redTurret.draw(win)
    blueTurret.draw(win)
    redTower.draw(win)
    blueTower.draw(win)

    for skill in man.skills:
        skill.draw(win)

    for minion in minionsPlayer:
        minion.draw(win)
    for minion in minionsEnemy:
        minion.draw(win)

    man.draw(win)
    ene.draw(win)

    pygame.display.update()



def playerAttack():
    keys = pygame.key.get_pressed()
    # giam thoi gian hoi chieu cua ba chieu

    man.Q = 0 if man.Q <= 0 else man.Q - 1
    man.W = 0 if man.W <= 0 else man.W - 1
    man.E = 0 if man.E <= 0 else man.E - 1

    #tan cong neu nut chieu duoc an va thoi gian hoi chieu bang 0
    if keys[pygame.K_e] and man.E == 0:
        man.attack(win, "E", man.x, man.y, pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10)
    elif keys[pygame.K_w] and man.W == 0:
        man.attack(win, "W", man.x, man.y, pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10)
    elif keys[pygame.K_q] and man.Q == 0:
        man.attack(win, "Q", man.x, man.y, pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10)

def settings():
    run = True
    change = False
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            change = True
    return (run, change)

def ktraHitBox(a, b):
    if a.hitbox[0] <= b.hitbox[0] and a.hitbox[0] + a.hitbox[2] >= b.hitbox[0] and a.hitbox[1] <= b.hitbox[1] and a.hitbox[1] + a.hitbox[3] >= b.hitbox[1]:
        return True
    return False

def enemyAttack():
    ene.Q = 0 if ene.Q <= 0 else ene.Q - 1
    ene.W = 0 if ene.W <= 0 else ene.W - 1
    ene.E = 0 if ene.E <= 0 else ene.E - 1

    kc = calculator.khoangCach(ene.x, ene.y, man.x, man.y)

    if kc < 100 and ene.E == 0:
        ene.attack(win, "E", ene.x, ene.y, man.x + 10, man.y + 10)
    elif kc < 200 and ene.W == 0:
        ene.attack(win, "W", ene.x, ene.y, man.x + 10, man.y + 10)
    elif kc < 100 and man.Q == 0:
        ene.attack(win, "Q", ene.x, ene.y, man.x + 10, man.y + 10)

def playMove():
    global man
    global ene
    global minionsEnemy
    global minionsPlayer

    man.move(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], change)
    ene.move(man, time[0] * 60 + time[1])

    for minion in minionsPlayer:
        minion.move(ene, minionsEnemy)

    for minion in minionsEnemy:
        minion.move(man, minionsPlayer)

def playEvent():

    global minionsPlayer
    global minionsEnemy

    if (time[0] * 60 + time[1]) % 10 == 0 and time[2] == 0:
        minionsEnemy.append(mimion.Minion(False, 1239, 153))
        minionsPlayer.append((mimion.Minion(True, 152, 623)))

    playMove()

    for minion in minionsPlayer:
        minion.skills.append(skill.Skill(pygame.image.load(r"picture/bullet.png"), 5, minion.x, minion.y, ene.x,ene.y, 10, 1))
        for sk in minion.skills:
            if ktraHitBox(sk, man):
                man.hitted(sk)

    for minion in minionsEnemy:
        minion.skills.append(skill.Skill(pygame.image.load(r"picture/bullet.png"), 5, minion.x, minion.y, ene.x, ene.y, 10, 1))
        for sk in minion.skills:
            if ktraHitBox(sk, man):
                man.hitted(sk)

    for red in minionsPlayer:
        for blue in minionsEnemy:
            if ktraHitBox(red, blue):
                red.hitted(blue.skill[0])
                blue.hitted(red.skill[0])

    for sk in man.skills:
        if ktraHitBox(sk, ene) or ktraHitBox(ene, sk):
            ene.hitted(sk)

    minionsPlayer = list(filter(lambda x : x.tonTai, minionsPlayer[:])) #Loc cac doi tuong linh con song
    minionsEnemy = list(filter(lambda x: x.tonTai, minionsEnemy[:])) #Loc cac doi thuong linh con song
    ene.skills = list(filter(lambda x : x.tonTai, ene.skills[:]))
    man.skills = list(filter(lambda x : x.tonTai, man.skills[:]))


while run2:
    #set so
    clock2.tick(30)
    win.blit(bg, (0,0))

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run2 = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            run2 = False


while run:

    clock.tick(30)
    if time[2] == 30:
        time[1] += 1
        time[2] = 0
    if time[1] == 60:
        time[0] += 1
        time[1] = 0

    change = False
    run, change =  settings()

    playerAttack()
    enemyAttack()

    playEvent()

    redrawWindow(change)


    time[2] += 1

pygame.quit()




