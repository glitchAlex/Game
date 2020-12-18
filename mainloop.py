import pygame as pg
from class_game import *
from pygame import Vector2
from random import randrange
#pylint: disable=no-member

pg.init()

pygame.display.set_caption('Good guys vs. Bad guys')
win = pg.display.set_mode((800, 600))
bg = pg.image.load('first_game\\popa.jpg')
clock = pg.time.Clock()
camera = Vector2(400, 300)
Images = []
Images.append(pg.transform.scale((pg.image.load('first_game\\Spaceship_gay.png')),[70,70]))
Images.append(pg.transform.scale((pg.image.load('first_game\\Enemy_gay.png')),[70,70]))
Images.append(pg.transform.scale((pg.image.load('first_game\\Vzryv.png')),[70,70]))
Images.append(pg.transform.scale((pg.image.load('first_game\\Schit.png')),[70,70]))

background_rects = [pg.Rect(randrange(-3000, 3001), randrange(-3000, 3001), 20, 20)
                    for _ in range(500)]
#song = pg.mixer.Sound('Loyalty Freak Music - It feels good to be alive too.mp3')
#song.play()

run = True
delay = 20
all_sprites = pg.sprite.Group()
player = Hero([400.0,300.0],5,True, Images)
cdPlayerShoot = 0
cdPlayerShield = 15000
enemies = []
cdEnemies = []
step = []
randal = Hero([400.0,100.0], 1, False, Images) #randal setting
enemies.append(randal) #randal setting
cdEnemies.append(0) #randal setting
step.append(0) #randal setting
bullets = []
speed = 10
delay_counter = 0
while run:
    pg.time.delay(delay)
    delay_counter+=delay
    print(delay_counter)

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
        '''
        for npc in enemies:
            npc.Move(0,-speed)
        '''
    if keys[pg.K_d]: #moving right
        player.Move(speed,0)
        '''
        for npc in enemies:
            npc.Move(0,-speed)
        '''
    if keys[pg.K_s]: #moving down
        player.Move(0,speed)
        '''
        for npc in enemies:
            npc.Move(0,-speed)
        '''
    if keys[pg.K_w]: #moving up
        player.Move(0,-speed)
        '''
        for npc in enemies:
            npc.Move(0,-speed)
        '''
    if keys[pg.K_SPACE] and (cdPlayerShield == 15000): #shielding
        cdPlayerShield = 0
        player.Shield(modeOn=True)
    if (keys[pg.K_q] or keys[pg.K_e]) and (cdPlayerShoot == 0): #shooting
        tmp = player.Shoot(keys, offset)
        bullets.append(tmp[0]) #fix to use shotgun
        cdPlayerShoot = tmp[1]
    
    #object and enemy proccessing
    for bull in bullets[:]: #hitting enemies
        hit = False
        for npc in enemies:
            if npc.Ishit(bull, offset):
                npc.Damage()
                hit = True
        if hit:
            bullets.remove(bull)
    for npc in enemies[:]: #removing dead enemies
        if (not npc.Status()) and (not npc.StatusCrit()):
            enemies.remove(npc)
            npc.__del__()
    for npc in enemies: #buzzing?
        if delay_counter%(2*4*delay) == 0*delay:
            npc.Move(-speed,0)
        if delay_counter%(2*4*delay) == 2*1*delay:
            npc.Move(0,speed)
        if delay_counter%(2*4*delay) == 2*2*delay:
            npc.Move(speed,0)
        if delay_counter%(2*4*delay) == 2*3*delay:
            npc.Move(0,-speed)
    if cdPlayerShoot > 0: #cd shoot proccesings
        cdPlayerShoot-=1
    if cdPlayerShield < 15000: #cd shield proccesings
        cdPlayerShield+=delay
    if cdPlayerShield > 1000 and player.is_protected == True: #getting Shield off
        player.Shield()
    for bull in bullets: #bullets move
        bull.Move(5)
    for bull in bullets[:]: #bullets delete
        if not bull.is_in():
            bullets.remove(bull)
            bull.__del__()
    #print(delay_counter)
    if delay_counter%10*delay == 0: #shooting enemy
        print('cool')
        for npc in enemies:
            print('cooler')
            tmp = npc.Shoot(keys, offset)
            bullets.append(tmp[0])
    
    #printing
    #print(bullets)
    #print(enemies)
    #print(cdPlayerShield)
    #print(player.is_protected)
    win.blit(bg,(0,0))
    for i in range(len(bullets)): #print bullets
        pg.draw.circle(win, (0,255,0), bullets[i].coord, 5)
        pg.draw.circle(win, (255,255,255), bullets[i].coord, 3)
        pg.draw.circle(win, (0,0,0), bullets[i].coord, 1)
    for background_rect in background_rects: #print rocks
            topleft = background_rect.topleft + offset
            pg.draw.rect(win, (200, 50, 70), (topleft, background_rect.size))
    clock.tick(60)
    player.blit_me(win, offset)
    for npc in enemies:
        npc.blit_me(win,offset)
    pg.display.update()
    
pg.quit()
