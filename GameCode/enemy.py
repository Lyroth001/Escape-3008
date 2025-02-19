import random
import json
from pygame import *
from attacks import bullet
class enemy(sprite.Sprite):
    #enemy is designed to be a generic superclass used by each enemy object
    def __init__(self,hp,atkpwr,atkspd,movspd,colour,name,screen,enemyGroup,bulletGroup,score=0):
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
        self.atktimer = atkspd
        self.score=score

    def enemyInit(self,player):
        #sets the enemy location and assigns the player
        self.loc = [random.randint(32*3,32*30),random.randint(32*3,32*10)]
        self.player = player
        self.screen.blit(self.sprite,(self.loc[0],self.loc[1]))
    
    def locatePlayer(self):
        return self.player.getLocation()
    
    def getHealth(self):
        return self.hp
    
    def takeDamage(self,damage):
        self.hp -= damage

    def getType(self):
        return "enemy"
    
    def onDeath(self):
        return self.score

    def takeTurn(self):
        #calculates direction of player in relation to self, used to move and attack
        dirc = []
        atkDirc=[]
        playerLoc=self.locatePlayer()
        xDiff=playerLoc[0]-self.loc[0]
        if xDiff>100 or xDiff<-100:
            if xDiff>0:
                dirc.append(1)
            elif xDiff<0:
                dirc.append(-1)
        else:
            if xDiff>0:
                atkDirc.append(1)
            elif xDiff<0:
                atkDirc.append(-1)
            dirc.append(0)
        yDiff=playerLoc[1]-self.loc[1]
        if yDiff>100 or yDiff<-100:
            if yDiff>0:
                dirc.append(1)
            elif yDiff<0:
                dirc.append(-1)
        else:
            if yDiff>0:
                atkDirc.append(1)
            elif yDiff<0:
                atkDirc.append(-1)
            dirc.append(0)
        if dirc != [0,0]:
            atkDirc=dirc
        self.move(dirc)
        self.rect.topleft=(self.loc[0],self.loc[1])
        if atkDirc != [0,0]:
            return self.attack(atkDirc)

    def attack(self,dirc):
        if self.atktimer == self.atkspd:
            self.atktimer = 0
            return bullet([self.loc[0]+16*dirc[0],self.loc[1]+16*dirc[1]],dirc,6,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
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


class turret(enemy):
    #same as enemy above, except it will not move
    def __init__(self,hp,atkpwr,atkspd,movspd,colour,name,screen,enemyGroup,bulletGroup,score=0):
        super().__init__(hp,atkpwr,atkspd,movspd,colour,name,screen,enemyGroup,bulletGroup,score)
    def takeTurn(self):
        dirc = []
        playerLoc=self.locatePlayer()
        xDiff=playerLoc[0]-self.loc[0]
        if xDiff>10 or xDiff < -10:
            if xDiff>0:
                dirc.append(1)
            elif xDiff<0:
                dirc.append(-1)
        else:
            dirc.append(0)
        yDiff=playerLoc[1]-self.loc[1]
        if yDiff>10 or yDiff<-10:
            if yDiff>0:
                dirc.append(1)
            elif yDiff<0:
                dirc.append(-1)
        else:
            dirc.append(0)
        self.rect.topleft=(self.loc[0],self.loc[1])
        self.screen.blit(self.sprite,(self.loc[0],self.loc[1]))
        if dirc != [0,0]:
            return self.attack(dirc)
