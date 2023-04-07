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

run = True
count = 0
minionsPlayer = []
minionsEnemy = []
skills = []


def redrawWindow(move):
    win.blit(bg, (0,0))

    for skill in man.skills:
        skill.draw(win)

    for minion in minionsPlayer:
        minion.draw(win, ene, minionsEnemy)
    for minion in minionsEnemy:
        minion.draw(win, man, minionsPlayer)

    ene.draw(win, man, minionsPlayer)
    man.draw(win, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], move)
    pygame.display.update()

def playerAttack(keys):

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



while run:
    clock.tick(30)
    if count == 0:
        minionsEnemy.append(mimion.Minion(False, 900))
        minionsPlayer.append(mimion.Minion(True, 0))
    count += 1
    if count == 300:
        count = 0
    move = False
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            move = True

    playerAttack(keys)

    redrawWindow(move)

pygame.quit()
