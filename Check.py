import pygame
import NewClass as p

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Проверка")

Images=[]

Images.append(pygame.transform.scale((pygame.image.load('C:\\Users\\Максим.DESKTOP-N5OPJQH\\Desktop\\Картинки к игре\\Spaceship.jpg')),[70,70]))
Images.append(pygame.transform.scale((pygame.image.load('C:\\Users\\Максим.DESKTOP-N5OPJQH\\Desktop\\Картинки к игре\\Enemy_gay.png')),[70,70]))

"""
for image in Images:
    image = pygame.transform.scale(image,[25,6])
   """ 
P = p.Hero([50,50],10, True,Images)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        P.Move(-10,0)
    if keys[pygame.K_RIGHT]:
        P.Move(10,0)
    win.fill((0,0,255))
    P.blit_me(win)
    pygame.display.update()
pygame.quit()
