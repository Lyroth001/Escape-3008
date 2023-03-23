#Classes for creating each level, using the map generator. Takes from the main BuildFloorInterface for actual generation
#but changes factors such as rooms and boss pool depending on each level
from enemy import *
from mapGen import *
class BuildLevel1(BuildFloorInterface):
    def __init__(self,x,y,rooms,seed,screen,enemyGroup,bulletGroup):
        self.screen = screen
        self.enemyGroup=enemyGroup
        self.bulletGroup=bulletGroup
        super().__init__(x,y,rooms,seed)
        self.__addEnemies()
        
    def __addEnemies(self):
        enemyOptions = []
        enemyOptions.append({"hp":10,"atkpwr":2,"atkspd":60,"movspd":1,"colour":(255,255,255),"moveops":(0,1),"name":"enemy","screen":self.screen,"enemyGroup":self.enemyGroup,"bulletGroup":self.bulletGroup})
        self.enemies = enemyOptions
        self.floorPlan.setEnemies(enemyOptions)
        print(self.enemies)

    