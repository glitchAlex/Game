class Hero:
    def __init__(self, coord, health, max_health, is_alive):
        self.coord = coord
        self.health = max_health
        self.max_health = max_health
        self.is_alive = True
        self.is_protected = False
        self.weapon = {'blaster' = 10,
                       'shotgun' = 5,
                       'pg' = 1}
    def Distruction(self):
        self.is_alive = False
        #return self.is_alive
    def Status(self):
        return self.is_alive
    def Move (self, dx, dy):
        self.coord[0] += dx
        self.coord[1] += dy
        #return self.coord
    def Doctor (self):
        if self.health < self.max_health:
            self.health += 1
        #return self.health
    def Damage (self):
        if self.is_protected == False:
            if self.health > 1:
                self.health -= 1
                #return self.health
            else:
                self.is_alive = False
                #return self.is_alive
    def Shoot (self, button):
        if button == '1':
            curr_weapon = self.weapon['blaster']
        if button == '2':
            curr_weapon = self.weapon['shotgun']
        if button == '3':
            curr_weapon = self.weapon['pg']
    def Shild (self):
        self.is_protected = True
        #return self.is_protected
    
class Bullet:
    def __init__(self, coord):
        self.coord = coord
    def Move (self, dy):
        self.coord[1] += dy
P = Hero(3,3,10,10)
P.Damage()
print(P.health)
