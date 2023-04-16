from pygame import *
from enemy import *
from items import newFloor
import random
class boss(enemy):
    def __init__(self,hp,atkpwr,atkspd,movspd,colour,name,screen,enemyGroup,bulletGroup,score=0):
        super().__init__(hp,atkpwr,atkspd,movspd,colour,name,screen,enemyGroup,bulletGroup,score)
    
    def onDeath(self):
        pass

class doctor(boss):
    def __init__(self,hp,atkpwr,atkspd,movspd,name,screen,enemyGroup,bulletGroup,colour=(0,0,0),score=0):
        super().__init__(hp,atkpwr,atkspd,movspd,colour,name,screen,enemyGroup,bulletGroup,score)

    def bossInit(self,player):
        self.loc = [random.randint(32*3,32*30),random.randint(32*3,32*10)]
        self.player=player

    def takeTurn(self):
        #as enemy, except selects between possible attack options and executes one of them
        toTake = random.randint(1,10)
        dirc = []
        playerLoc=super().locatePlayer()
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
        if toTake == 1:
            self.atk1()
        if toTake == 2:
            self.atk2()
        if toTake == 3:
            self.atk3()
        else:
            self.atk4(dirc)

    def atk1(self):
    #row of bullets across screen horiz
        if self.atktimer == self.atkspd:
            self.atktimer = 0
            for x in range(1,31,3):
                if x%2==0:
                    upDown=-1
                else:
                    upDown=1
                bullet([32*x,self.loc[1]],[0,upDown],32,(255,0,255),1,self.dmg,self.screen,self.bulletGroup)
        else:
            self.atktimer+=1
    
    def atk2(self):
    #row of bullets across screen vert
        pass
        if self.atktimer == self.atkspd:
            self.atktimer = 0
            for x in range(1,19,3):
                if x%2==0:
                    upDown=-1
                else:
                    upDown=1
                bullet([self.loc[0],32*x],[upDown,0],32,(255,0,255),1,self.dmg,self.screen,self.bulletGroup)
        else:
            self.atktimer+=1
    def atk3(self):
    #bullets in 8 directions
        if self.atktimer == self.atkspd:
            self.atktimer = 0
            bullet([self.loc[0]-20,self.loc[1]-20],[-1,-1],8,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
            bullet([self.loc[0],self.loc[1]-20],[0,-1],8,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
            bullet([self.loc[0]+20,self.loc[1]-20],[1,-1],8,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
            bullet([self.loc[0]-20,self.loc[1]],[-1,0],8,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
            bullet([self.loc[0]+20,self.loc[1]],[1,0],8,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
            bullet([self.loc[0]-20,self.loc[1]+20],[-1,1],8,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
            bullet([self.loc[0],self.loc[1]+20],[0,1],8,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
            bullet([self.loc[0]+20,self.loc[1]+20],[1,1],8,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
        else:
            self.atktimer += 1

    def atk4(self,dirc):
        #standard single bullet attack
        if self.atktimer == self.atkspd:
            self.atktimer = 0
            bullet([self.loc[0]+32*dirc[0],self.loc[1]+32*dirc[1]],dirc,6,(255,0,255),2,self.dmg,self.screen,self.bulletGroup)
        else:
            self.atktimer += 1

    def onDeath(self,tier,enemyGroup,enemyBullet,bossGroup):
        #increases the players score and generates a new floor item, allowing further progression
        self.player.gainScore(self.score)
        return newFloor("nextLevel",self.player,(0,0,0),tier+1,enemyGroup,enemyBullet,bossGroup)
