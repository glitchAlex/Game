import pygame as pg
from class_game import *
from pygame import Vector2
from random import randrange
#pylint: disable=no-member

pg.init()

win = pg.display.set_mode((800, 600))
bg = pg.image.load('first_game\\popa.jpg')
clock = pg.time.Clock()
camera = Vector2(400, 300)
Images = []
Images.append(pg.transform.scale((pg.image.load('first_game\\Spaceship_gay.png')),[70,70]))
Images.append(pg.transform.scale((pg.image.load('first_game\\Enemy_gay.png')),[70,70]))

background_rects = [pg.Rect(randrange(-3000, 3001), randrange(-3000, 3001), 20, 20)
                    for _ in range(500)]
#song = pg.mixer.Sound('Loyalty Freak Music - It feels good to be alive too.mp3')
#song.play()

run = True
delay = 20
all_sprites = pg.sprite.Group()
player = Hero([400,300],5,True, Images, is_protected=True)
cdPlayerShoot = 0
cdPlayerShield = 0
enemies = []
testenemy = Hero([400,200], 1, True, Images)
enemies.append(testenemy)
cdEnemies = []
cdEnemies.append(0)
bullets = []
speed = 10
while run:
    pg.time.delay(delay)

    for event in pg.event.get():
        if event.type == pg.QUIT: #quiting game via close button
            run = False
    all_sprites.update()
    heading = player.coord - camera
    camera += heading * 0.05
    offset = -camera + Vector2(400, 300)
    keys = pg.key.get_pressed()

    #player actions
    if keys[pg.K_a]: #moving left
        player.Move(-speed,0)
    if keys[pg.K_d]: #moving right
        player.Move(speed,0)
    if keys[pg.K_s]: #moving down
        player.Move(0,speed)
    if keys[pg.K_w]: #moving up
        player.Move(0,-speed)
    if keys[pg.K_SPACE]: #shielding
        player.Shield(modeOn=True)
    if (keys[pg.K_q] or keys[pg.K_e]) and (cdPlayerShoot == 0): #shooting
        tmp = player.Shoot(keys, offset)
        bullets.append(tmp[0]) #fix to use shotgun
        cdPlayerShoot = tmp[1]
    
    #object and enemy proccessing
    #enemy loop
    #print(cdPlayerShoot)
    if cdPlayerShoot > 0: #cd shoot proccesings
        cdPlayerShoot-=1
    for bull in bullets:
        bull.Move(5)
    
    #print(bullets)
    #printing
    win.blit(bg,(0,0))
    for i in range(len(bullets)):
        #print(bullets[i].coord)
        pg.draw.circle(win, (0,255,0), bullets[i].coord, 5)
        pg.draw.circle(win, (255,255,255), bullets[i].coord, 3)
        pg.draw.circle(win, (0,0,0), bullets[i].coord, 1)
    for background_rect in background_rects:
            topleft = background_rect.topleft + offset
            pg.draw.rect(win, (200, 50, 70), (topleft, background_rect.size))
    clock.tick(60)
    #pygame.draw.rect(win, (255,255,255), (0, 0, 80, 60)) #useless line
    player.blit_me(win, offset)
    pg.display.update()
    
pg.quit()