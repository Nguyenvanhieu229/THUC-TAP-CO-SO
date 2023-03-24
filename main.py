import pygame
import player
import mimion
pygame.init()

#Hieu sua thu
#Hieru thu tiep

win = pygame.display.set_mode((900, 500))
bg = pygame.image.load(r"C:\Users\admin\Pictures\TTCS\bg.jpg")
clock = pygame.time.Clock()
man = player.Player()

run = True
count = 0
minions = []


def redrawWindow(move):
    win.blit(bg, (0,0))
    for minion in minions:
        minion.draw(win)
    man.draw(win, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], move)
    pygame.display.update()

def playerAttack(keys):

    # giam thoi gian hoi chieu cua ba chieu
    man.Q = 0 if man.Q <= 0 else man.Q - 1
    man.W = 0 if man.W <= 0 else man.W - 1
    man.E = 0 if man.E <= 0 else man.E - 1

    #tan cong neu nut chieu duoc an va thoi gian hoi chieu bang 0
    if keys[pygame.K_e] and man.E == 0:
        man.attack(win, "E")
    elif keys[pygame.K_w] and man.W == 0:
        man.attack(win, "W")
    elif keys[pygame.K_q] and man.Q == 0:
        man.attack(win, "Q")

while run:
    clock.tick(30)
    if count == 0 or count == 5 or count == 10:
        minions.append(mimion.Minion(False, 900))
        minions.append(mimion.Minion(True, 0))
    count += 1
    if count == 300:
        count = 0
    move = False
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            move = True
    playerAttack(keys)

    redrawWindow(move)

pygame.quit()