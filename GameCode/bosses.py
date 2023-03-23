from pygame import *
from enemy import enemy
import random
class boss(enemy):
    def __init__(self,hp,atkpwr,atkspd,movspd,colour,moveoptions,name,screen,enemyGroup,bulletGroup):
        super.__init__(hp,atkpwr,atkspd,movspd,colour,moveoptions,name,screen,enemyGroup,bulletGroup)

class doctor(boss):
    def __init__(self,hp,atkpwr,atkspd,movspd,colour,moveoptions,name,screen,enemyGroup,bulletGroup):
        super.__init__(hp,atkpwr,atkspd,movspd,colour,moveoptions,name,screen,enemyGroup,bulletGroup)


    def takeTurn(self):
        toTake = random.randint(1,3)
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
        if toTake == 1:
            self.atk1()
        if toTake == 2:
            self.atk2()
        else:
            self.atk3()
        
        
    def atk1(self):
        pass
    def atk2(self):
        pass
    def atk3(self):
        pass