class Hero:     #создает класс персонажа (и доброго, и злого)
    def __init__(self, coord, health, max_health, is_good, Images, is_alive = True, is_protected = False):    #координаты, здоровье, максимальное здоровье, добрый или злой (1 или 2),
        self.coord = coord                                                                                    #живой ли, включен ли щит, ссылка на картинки
        self.health = max_health
        self.max_health = max_health
        self.is_good = is_good
        self.is_alive = True
        self.is_protected = False
        self.images = Images
        self.weapon = {"blaster" : 10,
                       'shotgun' : 5,
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
        return self.is_good == 1
    def blit_me(self, display_surface):    #рисует на экране
        if self.is_main == True:
            display_surface.blit(self.images[0],(self.coord[0],self.coord[1]))
        else:
            display_surface.blit(self.images[1],(self.coord[0],self.coord[1]))
    def Distruction(self):    #уничтожение
        self.is_alive = False
        #return self.is_alive
    def Status(self):    #текущий статус
        return self.is_alive
    def Move (self, dx, dy):    #перемещение
        if (self.coord[0]>0)&(self.coord[0]<500):
            self.coord[0] += dx
        if (self.coord[0]>0)&(self.coord[0]<780):
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
    def Shoot (self, button):    #выстрел
        if button == '1':
            curr_weapon = self.weapon['blaster']
        if button == '2':
            curr_weapon = self.weapon['shotgun']
        if button == '3':
            curr_weapon = self.weapon['pg']
        return curr_weapon
    def Shield (self):    #щит
        self.is_protected = True
        #return self.is_protected
    
class Bullet:
    def __init__(self, coord):
        self.coord = coord
    def Move (self, dy):
        self.coord[1] += dy
