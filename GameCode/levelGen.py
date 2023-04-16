#Classes for creating each level, using the map generator. Takes from the main BuildFloorInterface for actual generation
#but changes factors such as rooms and boss pool depending on each level
from mapGen import *
class BuildLevel1(BuildFloorInterface):
    def __init__(self,x,y,rooms,seed,tier,screen,enemyGroup,bulletGroup,bossGroup):
        self.screen = screen
        self.tier=tier*3
        self.enemyGroup=enemyGroup
        self.bulletGroup=bulletGroup
        self.bossGroup=bossGroup
        super().__init__(x,y,rooms,self.tier,seed)
        self.__addEnemies()
        
    def __addEnemies(self):
        #builds dicts of enemy and boss options to be assembled into objects when required
        enemyOptions = []
        enemyOptions.append({"hp":10+self.tier,"atkpwr":2+self.tier-3,"atkspd":60,"movspd":1,"colour":(255,255,255),"name":"enemy","screen":self.screen,"enemyGroup":self.enemyGroup,"bulletGroup":self.bulletGroup,"score":50+self.tier})
        enemyOptions.append({"hp":10+self.tier,"atkpwr":2+self.tier-3,"atkspd":60,"movspd":0,"colour":(150,150,255),"name":"turret","screen":self.screen,"enemyGroup":self.enemyGroup,"bulletGroup":self.bulletGroup,"score":50+self.tier})
        bossOptions=[]
        bossOptions.append({"hp":30+self.tier*2,"atkpwr":5+self.tier,"atkspd":30,"movspd":5,"name":"Doctor","screen":self.screen,"bossGroup":self.bossGroup,"bulletGroup":self.bulletGroup,"score":500+self.tier})
        self.enemies = enemyOptions
        self.floorPlan.setBosses(bossOptions)
        self.floorPlan.setEnemies(enemyOptions)

    