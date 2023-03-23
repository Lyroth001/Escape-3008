from pygame import *
import random
class item(sprite.Sprite):
    def __init__(self,name,player,colour, *groups):
        self.name=name
        super().__init__(*groups)
        self.sprite=Surface((16,16), SRCALPHA, 32).convert_alpha()
        draw.rect(self.sprite,colour,(16,16),16)
        self.rect=self.sprite.get_rect()
        self.player=player
    
    def onPickup(self):
        #base method for item to apply its effect
        pass

class healthBoost(item):
    def __init__(self,player,healthRestored, *groups):
        super().__init__(*groups)
        self.player=player
        self.healing=healthRestored
    
    def onPickup(self):
        self.player.gainHealth(self.healing)

class atkBoost(item):
    def __init__(self,player,atkBoostGive, *groups):
        super().__init__(*groups)
        self.player=player
        self.atkUp=atkBoostGive
    
    def onPickup(self):
        self.player.gainAtk(self.atkUp)

def assignItem(player,tier):
    itemList=[healthBoost(player,random.randint(0,tier))]
    return itemList[random.randint(0,len(itemList)-1)]