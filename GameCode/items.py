from pygame import *
import random
class item(sprite.Sprite):
    def __init__(self,name,player,colour):
        self.name=name
        super().__init__()
        self.sprite=Surface((16,16), SRCALPHA, 32).convert_alpha()
        self.w, self.h = display.get_surface().get_size()
        print(self.w,self.h)
        draw.circle(self.sprite,colour,(8,8),16)
        self.rect=self.sprite.get_rect()
        self.rect.topleft=(self.w/2,self.h/2)
        self.player=player

    def itemIdle(self,screen):
        screen.blit(self.sprite,(self.w/2,self.h/2))
    
    def onPickup(self):
        #base method for item to apply its effect
        
        pass

class healthBoost(item):
    def __init__(self,name,player,colour,healthRestored):
        super().__init__(name,player,colour)
        self.player=player
        self.healing=healthRestored
    
    def onPickup(self):
        print(f"{self.name} activating")
        self.player.gainHealth(self.healing)

class atkBoost(item):
    def __init__(self,name,player,colour,atkBoostGive):
        super().__init__(name,player,colour)
        self.player=player
        self.atkUp=atkBoostGive
    
    def onPickup(self):
        print(f"{self.name} activating")
        self.player.gainAtk(self.atkUp)

def assignItem(player,tier):
    itemList=[healthBoost("Health up",player,(50,255,50),random.randint(1,tier)),atkBoost("Attack up",player,(50,255,255),random.randint(1,tier))]
    return itemList[random.randint(0,len(itemList)-1)]