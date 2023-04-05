import pygame
import player
import mimion
import skill
pygame.init()

#Hieu sua thu
#Hieru thu tiep
# asdads

win = pygame.display.set_mode((1800, 1000))
bg = pygame.image.load(r"picture\bg.jpg")
clock = pygame.time.Clock()
man = player.Player()

run = True
count = 0
minions = []
skills = []


def redrawWindow(move):
    win.blit(bg, (0, 0))
    man.draw(win, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], move)
    for skill in man.skills:
        skill.draw(win)

    for minion in minions:
        minion.draw(win)
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
    if count == 0 or count == 5 or count == 10:
        minions.append(mimion.Minion(False, 900))
        minions.append(mimion.Minion(True, 0))
    count += 1
    if count == 300:
        count = 0
    keys = pygame.key.get_pressed()
    move = False
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            move = True
    redrawWindow(move)
    playerAttack(keys)


pygame.quit()
