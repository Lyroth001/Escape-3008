#Classes for creating each level, using the map generator. Takes from the main BuildFloorInterface for actual generation
#but changes factors such as rooms and boss pool depending on each level
from enemy import *
from mapGen import *
from bosses import *
class BuildLevel1(BuildFloorInterface):
    def __init__(self,x,y,rooms,seed,tier,screen,enemyGroup,bulletGroup,bossGroup):
        self.screen = screen
        self.enemyGroup=enemyGroup
        self.bulletGroup=bulletGroup
        self.bossGroup=bossGroup
        tier=tier*3
        super().__init__(x,y,rooms,tier,seed)
        self.__addEnemies()
        
    def __addEnemies(self):
        enemyOptions = []
        enemyOptions.append({"hp":10,"atkpwr":2,"atkspd":60,"movspd":1,"colour":(255,255,255),"name":"enemy","screen":self.screen,"enemyGroup":self.enemyGroup,"bulletGroup":self.bulletGroup,"score":50})
        #bossOptions=[doctor(30,5,5,5,"Doctor",self.screen,self.bossGroup,self.bulletGroup,score=500)]
        bossOptions=[]
        bossOptions.append({"hp":30,"atkpwr":5,"atkspd":30,"movspd":5,"name":"Doctor","screen":self.screen,"bossGroup":self.bossGroup,"bulletGroup":self.bulletGroup,"score":500})
        self.enemies = enemyOptions
        self.floorPlan.setBosses(bossOptions)
        self.floorPlan.setEnemies(enemyOptions)

    