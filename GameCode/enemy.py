import random
import json
from pygame import *
from attacks import bullet
class enemy(sprite.Sprite):
    #enemy is designed to be a generic superclass used by each enemy object
    def __init__(self,hp,atkpwr,atkspd,movspd,colour,moveoptions,name,screen,enemyGroup,bulletGroup):
        sprite.Sprite.__init__(self,enemyGroup)
        #atk speed is an amount of ticks before can attack again, based on iterations of takeTurn()
        self.hp = hp
        self.dmg = atkpwr
        self.atkspd = atkspd
        self.bulletGroup=bulletGroup
        self.movspd = movspd
        self.sprite = Surface((32,32), SRCALPHA, 32).convert_alpha()
        draw.circle(self.sprite,colour,(16,16),16)
        self.rect=self.sprite.get_rect()
        self.name = name
        self.screen = screen
        #moveoptions should be tuple
        self.movops = moveoptions
        self.atktimer = atkspd

    def enemyInit(self,player):
        self.loc = [random.randint(32*3,32*30),random.randint(32*3,32*10)]
        self.player = player
        self.screen.blit(self.sprite,(self.loc[0],self.loc[1]))
    
    def locatePlayer(self):
        return self.player.getLocation()
    
    def takeDamage(self,damage):
        self.hp -= damage

    def getType(self):
        return "enemy"

    def takeTurn(self):
        toTake = random.randint(self.movops[0],self.movops[1])
        dirc = []
        playerLoc=self.locatePlayer()
        xDiff=playerLoc[0]-self.loc[0]
        if xDiff>100 or xDiff<-100:
            if xDiff>0:
                dirc.append(1)
            elif xDiff<0:
                dirc.append(-1)
        else:
            dirc.append(0)
        yDiff=playerLoc[1]-self.loc[1]
        if yDiff>100 or yDiff<-100:
            if yDiff>0:
                dirc.append(1)
            elif yDiff<0:
                dirc.append(-1)
        else:
            dirc.append(0)
        self.move(dirc)
        self.rect.topleft=(self.loc[0],self.loc[1])
        if dirc != [0,0]:
            return self.attack(dirc)

    def attack(self,dirc):
        if self.atktimer == self.atkspd:
            self.atktimer = 0
            return bullet([self.loc[0]+16*dirc[0],self.loc[1]+16*dirc[1]],dirc,3,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
        else:
            self.atktimer += 1

    def move(self,direction):
        self.loc[0] += direction[0]*self.movspd
        self.loc[1] += direction[1]*self.movspd
        self.screen.blit(self.sprite,(self.loc[0],self.loc[1]))

    def checkCol(self,collider):
        if collider.collidepoint(self.loc):
            return True
        else:
            return False
        
    def onDeath(self):
        pass

class turret(enemy):
    def __init__(self,hp,atkpwr,atkspd,movspd,strtloc,colour,moveoptions,name,screen):
        super.__init__(self,hp,atkpwr,atkspd,movspd,strtloc,colour,moveoptions,name,screen)
    def takeTurn(self):
        self.attack()
        
class rusher(enemy):
    def __init__(self,hp,atkpwr,atkspd,movspd,strtloc,colour,moveoptions,name,screen):
        super.__init__(self,hp,atkpwr,atkspd,movspd,strtloc,colour,moveoptions,name,screen)
    def takeTurn(self):
        dirc=[]
        playerLoc=self.locatePlayer()
        xDiff=playerLoc[0]-self.loc[0]
        if xDiff>30 or xDiff<-30:
            if xDiff>0:
                dirc.append(1)
            elif xDiff<0:
                dirc.append(-1)
        else:
            dirc.append(random.randint(-1,1))
        yDiff=playerLoc[1]-self.loc[1]
        if yDiff>30 or yDiff<-30:
            if yDiff>0:
                dirc.append(1)
            elif yDiff<0:
                dirc.append(-1)
        else:
            dirc.append(random.randint(-1,1))
        self.move(dirc)

class boss(enemy):
    #class all boss enemies should inherit from
    def __init__(self,hp,atkpwr,atkspd,movspd,strtloc,colour,moveoptions,name,screen):
        super.__init__(self,hp,atkpwr,atkspd,movspd,strtloc,colour,moveoptions,name,screen)
    
    def onDeath(self):
        pass