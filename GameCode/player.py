from pygame import *
from classes import *
from attacks import bullet
init()
class player(sprite.Sprite):
    def __init__(self,speed,strtHealth,strtDmg,atkspd,maxBullet,strtLoc,screen,bulletGroup):
        #maybe pull these from a bin file?
        sprite.Sprite.__init__(self)
        self.sprite = Surface((32,32), SRCALPHA, 32).convert_alpha()
        draw.circle(self.sprite,(50,0,255),(16,16),16)
        self.rect=self.sprite.get_rect()
        self.Group=bulletGroup
        self.speed = speed
        self.maxBullet = maxBullet
        self.bulletNum = 0
        self.bulletSpd = 1
        self.hp = strtHealth
        self.dmg = strtDmg
        self.dmgCooldown = 120 #At 60fps this should give 2 secs of I-frames upon being hit
        self.dmgCount=0
        self.atkBeat = 0
        self.atkSpd=atkspd
        self.loc = strtLoc
        self.screen = screen
        self.screen.blit(self.sprite,(self.loc[0],self.loc[1]))
        
    def movePlayer(self,direction):
        self.loc[0] += direction[0]*self.speed
        self.loc[1] += direction[1]*self.speed
        self.screen.blit(self.sprite,(self.loc[0],self.loc[1]))

    def setPlayerLoc(self,newLoc):
        self.loc = newLoc
        self.screen.blit(self.sprite,(self.loc[0],self.loc[1]))
        print(self.loc)

    def takeDamage(self,damage):
        if self.dmgCount == 0:
            self.hp -= damage
            self.dmgCount = self.dmgCooldown
    
    def gainHealth(self,healing):
        self.hp+=healing
    
    def getHp(self):
        return self.hp

    def gainAtk(self,boost):
        self.dmg+=boost

    def getAtk(self):
        return self.dmg

    def getSpeed(self):
        return self.speed

    def playerIdle(self):
        self.screen.blit(self.sprite,(self.loc[0],self.loc[1]))
        self.passBeat()
        self.rect.topleft=(self.loc[0],self.loc[1])

    def getLocation(self):
        return self.loc

    def checkHitbox(self):
        return Rect(self.loc,(32,32))

    def shoot(self,direction):
        self.atkBeat = 0
        if self.bulletNum != self.maxBullet:
            self.bulletNum += 1
            return bullet([self.loc[0]+16*direction[0],self.loc[1]+16*direction[1]],direction,8,(50,255,50),self.bulletSpd,self.dmg,self.screen,self.Group)
        else:
            self.bulletNum=0
            return bullet([self.loc[0]+16*direction[0],self.loc[1]+16*direction[1]],direction,8,(50,255,50),self.bulletSpd,self.dmg,self.screen,self.Group)

    def checkBeat(self):
        return self.atkBeat

    def checkOnBeat(self):
        if self.checkBeat() == self.atkSpd:
            return True

    def passBeat(self):
        if self.atkBeat != self.atkSpd:
            self.atkBeat += 1
        if self.dmgCount >0:
            self.dmgCount -= 1
    
    def checkCol(self,collider):
        colliderBox=Rect((32,32),(self.loc[0],self.loc[1]))
        if colliderBox.collidepoint(collider):
            return True
        else:
            return False
