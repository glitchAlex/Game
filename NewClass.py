import pygame

class Bullet:
    def __init__(self, coord):
        self.coord = coord
    def Move (self, dy):
        self.coord[1] += dy    

class Hero:     #создает класс персонажа (и доброго, и злого)
    def __init__(self, coord, max_health, is_good, Images, is_alive = True, is_protected = False):    #координаты, здоровье, максимальное здоровье, добрый или злой (True или False),
        self.coord = coord                                                                                    #живой ли, включен ли щит, ссылка на картинки
        self.health = max_health
        self.max_health = max_health
        self.is_good = is_good
        self.is_alive = True
        self.is_protected = False
        self.images = Images
        self.weapon = {"blaster" : 10,
                       'pg' : 1}
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
        return is_good
    def blit_me(self, display_surface):    #рисует на экране
        if self.is_alive == True:
            if self.is_main == True:
                display_surface.blit(self.images[0],(self.coord[0],self.coord[1]))
            else:
                display_surface.blit(self.images[1],(self.coord[0],self.coord[1]))
        else:
            pass
    def Distruction(self):    #уничтожение
        self.is_alive = False
        #return self.is_alive
    def Status(self):    #текущий статус
        return self.is_alive
    def Move (self, dx, dy):    #перемещение
        if (self.coord[0]+dx>-50)&(self.coord[0]+dx<500-50):
            self.coord[0] += dx
        if (self.coord[1]+dy>0)&(self.coord[1]+dy<780):
            self.coord[1] += dy
        #return self.coord
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
        if keys[pygame.K_1]:
            curr_weapon = self.weapon['blaster']
        if keys[pygame.K_2]:
            curr_weapon = self.weapon['pg']
        tmp = Bullet(self.coord)
        return [tmp, curr_weapon]
    def Shield (self):    #щит
        self.is_protected = True
        #return self.is_protected
    

