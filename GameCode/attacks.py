#TODO Will not work, finish implementing sprites

from pygame import *
class bullet(sprite.Sprite):
    def __init__(self,strtcoords,direction,radius,colour,spd,dmg,screen,bulletGroup):
        #player is bool, essentailly says what a bullet can hit
        #friendly fire is not a thing
        sprite.Sprite.__init__(self,bulletGroup)
        self.coords=strtcoords
        self.sprite=Surface((16,16), SRCALPHA, 32).convert_alpha()
        draw.circle(self.sprite,colour,(8,8),8)
        self.rect=self.sprite.get_rect()
        self.speed=spd
        self.direction=direction
        self.dmg=dmg
        self.screen=screen

    def getType(self):
        return("attack")

    def takeTurn(self, id=None):
        self.move()

    def move(self):
        self.coords[0]+=self.direction[0]*self.speed
        self.coords[1]+=self.direction[1]*self.speed
        self.rect.topleft=(self.coords[0],self.coords[1])
        self.screen.blit(self.sprite,(self.coords[0],self.coords[1]))

    def doDamage(self,target):
        target.takeDamage(self.dmg)
    
    def checkCol(self,collider):
        if collider.collidepoint(self.coords):
            return True
        else:
            return False
