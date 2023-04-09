import pygame
import player
import mimion
import enemy
import skill
pygame.init()

#Hieu sua thu
#Hieru thu tiep
# asdads

win = pygame.display.set_mode((1366, 768))
bg = pygame.image.load(r"picture/bacg.png")
clock = pygame.time.Clock()
man = player.Player()
ene = enemy.Enemy()
reset = 0

run = True
count = 0
minionsPlayer = []
minionsEnemy = []
skills = []
time = [0,0]


def redrawWindow(change):
    win.blit(bg, (0,0))

    for skill in man.skills:
        skill.draw(win)

    for minion in minionsPlayer:
        minion.draw(win)
    for minion in minionsEnemy:
        minion.draw(win)

    ene.draw(win)
    man.draw(win)
    pygame.display.update()



def playerAttack(keys):
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

while run:
    clock.tick(30)
    time[1]+=30
    if time[1] == 60:
        time[0] += 1
        time[1] = 60
    change = False
    run, change =  settings()
    playerAttack(keys)
    playEvent()
    redrawWindow(change)

pygame.quit()


def playEvent():
    man.move(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],change)
    ene.move(time[0]*60+time[1])
    if (time[0] * 60 + time[1]) % 600 == 0:
        minionsEnemy.append(mimion.Minion(True,100))
        minionsPlayer.append((mimion.Minion(False,900)))
    for enemyskill in ene.skills:
        if man.hitted(enemyskill):

