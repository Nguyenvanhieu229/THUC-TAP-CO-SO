import pygame
import player
import mimion
import enemy
import player
import skill
import tower
import mimion
import tru
pygame.init()

#Hieu sua thu
#Hieru thu tiep
# asdads

win = pygame.display.set_mode((1366, 768))
bg = pygame.image.load(r"picture/bacg.png")
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
man = player.Player()
ene = enemy.Enemy()
redturret = tru.Nha()
reset = 0

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
    redturret.draw(win)
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
def playEvent():
    man.move(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], change)
    ene.move(man, time[0]*60+time[1])
    if (time[0] * 60 + time[1]) % 600 == 0:
        minionsEnemy.append(mimion.Minion(False, 900))
        minionsPlayer.append((mimion.Minion(True, 100)))
    for minion in minionsPlayer:
        minion.skill.append(skill.Skill(pygame.image.load(r"picture/bullet.png"), 5, minion.x, minion.y, ene.x,ene.y, 10, 1))
        minion.move(ene, minionsEnemy)
        if ktraHitBox(minion, ene):
            #aaaaa
            ene.hitted(minion.skill)
    for minion in minionsEnemy:
        minion.move(man, minionsPlayer)
        minion.skill.append(skill.Skill(pygame.image.load(r"picture/bullet.png"), 5, minion.x, minion.y, ene.x, ene.y, 10, 1))
        if ktraHitBox(minion, man):
            man.hitted(minion.skill[0])
    for red in minionsPlayer:
        for blue in minionsEnemy:
            if ktraHitBox(red, blue):
                red.hitted(blue.skill[0])
                blue.hitted(red.skill[0])
    #print(man.health)

while run2:
    clock2.tick(30)
    win.blit(pygame.image.load(r"picture/bacg.png"), (0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run2 = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            run2 = False
while run:
    clock.tick(30)
    change = False
    run, change =  settings()
    playerAttack()
    playEvent()
    redrawWindow(change)
    if time[2] == 30:
        time[1] += 1
        time[2] = 0
    if time[1] == 60:
        time[0] += 1
        time[1] = 0
    time[2] += 1
    if time[2] == 30:
        print(time[0], time[1])
pygame.quit()




