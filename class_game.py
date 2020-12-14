import pygame
# pylint: disable=no-member

class Bullet:
    def __init__(self, coord, vec):
        self.coord = coord.copy()
        self.vec=vec
    def Move (self, dy):
        self.coord[1] += self.vec*dy    

class Hero:     #создает класс персонажа (и доброго, и злого)
    def __init__(self, coord, max_health, is_good, Images, is_alive = True, is_protected = False):    #координаты, здоровье, максимальное здоровье, добрый или злой (True или False),
        self.coord = coord                                                                                    #живой ли, включен ли щит, ссылка на картинки
        self.health = max_health
        self.max_health = max_health
        self.is_good = is_good
        self.is_alive = True
        self.is_protected = False
        self.images = Images
        self.weapon = {"blaster" : 50,
                       'pg' : 5}
    def __del__(self):    #деструктор
        del self.coord
        del self.health
        del self.max_health
        del self.is_good
        del self.is_alive
        del self.is_protected
        del self.images
        del self.weapon
    def is_main(self):    #проверка: добрый или злой
        return self.is_good
    def blit_me(self, display_surface, offset):    #рисует на экране
        if self.is_alive:
            if self.is_main():
                display_surface.blit(self.images[0],self.coord+offset)
            else:
                display_surface.blit(self.images[1],self.coord+offset)
        else:
            pass
    def Distruction(self):    #уничтожение
        self.is_alive = False
        #return self.is_alive
    def Status(self):    #текущий статус
        return self.is_alive
    def Move (self, dx, dy):    #перемещение
        #wip
        if (self.coord[0]+dx>-3100)&(self.coord[0]+dx<3101):
            self.coord[0] += dx
        if (self.coord[1]+dy>-3100)&(self.coord[1]+dy<3101):
            self.coord[1] += dy
        #return self.coord
        '''
        self.coord[0]+=dx
        self.coord[1]+=dy
        '''
    def Doctor (self):    #использование аптечки
        if self.health < self.max_health:
            self.health += 1
        #return self.health
    def Damage (self):    #получение урона
        if self.is_protected == False:
            if self.health > 1:
                self.health -= 1
                #return self.health
            else:
                self.is_alive = False
                #return self.is_alive
    def Shoot (self, keys):   #выстрел
        if keys[pygame.K_e]:
            curr_weapon = self.weapon['blaster']
        if keys[pygame.K_q]:
            curr_weapon = self.weapon['pg']
        if self.is_main():
            tmp = Bullet(self.coord, -1)
        else:
            tmp = Bullet(self.coord, 1)
        return [tmp, curr_weapon]
    def Shield (self, modeOn=False):    #щит
        if modeOn:
            self.is_protected = True
        else:
            self.is_protected = False
        #return self.is_protected