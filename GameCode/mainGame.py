#Potential idea- terminal interaction via unicurses, if completed succesfully gives free item
#Database behind encryption, completing levels grant decrypt?
#Main game module, creates window and handles userinputs, holds main game loop
#I will load all possible rooms immediatly, and then generate a hash value for each possible room
#to determine where in a dictionary or smthng they should be accessed
#check seed 65533925843339
#seed with item room by spawn 9046123406124146

#ADDED

import pygame
import os
import sys
from pygame.locals import * 
from levelGen import *
from classes import *
from player import player

class Escape3008:
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self._running=True
        self.size = self.width, self.height = 1024, 640
        self.collider = Rect((32,32),(self.width-94,self.height-94))
    #coord for room player is currently in
        self.playerLoc=[0,0]
    #coord for where on the screen the player is after pause
        self.playerCoords = [32,32]
    #stores the buttons currently on screen to be iterated through
        self.buttons=[]
        self.level = None
    #sets gamestate
        self.paused = False
        self.inMainMenu = True
        self.levelParameters=False
        self.inLevel = False
        self.database = False
        self.inMainGame = False
        self.mainMenuOptions = False
        self.levelOptions = False
        self.possibleRooms={}
        self.tier=1
    #Groups to hold visible objects and variables related to them
        self.enemies=pygame.sprite.Group()
        self.enemyBullets=pygame.sprite.Group()
        self.playerBullets=pygame.sprite.Group()
        self.items=pygame.sprite.Group()
        self.bosses=pygame.sprite.Group()

        self.font=pygame.font.SysFont("comicsans",30)
        self.uiFont=pygame.font.SysFont("segoeuisemibold",20)
        self.startButtonLoc=(50,240)
        print("running")

    def __on_init(self):
        #generates window+starts pygame
        pygame.init()
        self.surface=pygame.display.set_mode(self.size)
        pygame.display.set_caption("Escape 3008")
        self.__loadImages()
        self._running=True

    def getScreen(self):
        return self.surface
    
    def __on_event_menu(self, event):
        #Handles events during the menu screen
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            #manages player inputs
            if event.key==pygame.K_SPACE:
                self.seed=self.getSeedMenu()
                self.loadLevel(6,6,13,1,True)
                self.inMainMenu=False
                self.inMainGame=True
            elif event.key==pygame.K_ESCAPE:
                self._running = False
                self.inMainMenu = False
                pygame.quit()
            
                    
    def __on_event_game(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            #manages player inputs
            try:
                if event.key==pygame.K_ESCAPE:
                    self.inMainMenu=True
                    self.inMainGame=False
                    self.playerCoords=self.player.getLocation()
                elif event.key==pygame.K_g:
                    self._running = False
                    self.mainMenu = False
                    pygame.quit()
            except:
                print("Please generate a map with space before attempting to move")
   
    def gameKeyManager(self,key):
        #handles events for keypresses, controlling player movement and interaction
        currentLoc=self.player.getLocation()
        speed=self.player.getSpeed()
        if key[K_w] and key[K_a]:
            if self.collider.collidepoint(currentLoc[0]-(1*speed),currentLoc[1]-(1*speed)):
                self.player.movePlayer([-1,-1])
        elif key[K_w] and key[K_d]:
            if self.collider.collidepoint(currentLoc[0]+(1*speed),currentLoc[1]-(1*speed)):
                self.player.movePlayer([1,-1])
        elif key[K_w]:
            if self.collider.collidepoint(currentLoc[0],currentLoc[1]-(1*speed)):
                self.player.movePlayer([0,-1])
        elif key[K_d] and key[K_s]:
            if self.collider.collidepoint(currentLoc[0]+(1*speed),currentLoc[1]+(1*speed)):
                self.player.movePlayer([1,1])
        elif key[K_d]:
            if self.collider.collidepoint(currentLoc[0]+(1*speed),currentLoc[1]):
                self.player.movePlayer([1,0])
        elif key[K_s] and key[K_a]:
            if self.collider.collidepoint(currentLoc[0]-(1*speed),currentLoc[1]+(1*speed)):
                self.player.movePlayer([-1,1])
        elif key[K_s]:
            if self.collider.collidepoint(currentLoc[0],currentLoc[1]+(1*speed)):
                self.player.movePlayer([0,1])
        elif key[K_a]:
            if self.collider.collidepoint(currentLoc[0]-(1*speed),currentLoc[1]):
                self.player.movePlayer([-1,0])
        if key[K_q]:
            self.level.visualiseLevel()
        if key[K_LEFTBRACKET]:  
                self.clearGroups()
        if key[K_e]:
            if len(self.enemies)==0:
                currentRoomBits=self.level.rows[self.playerLoc[1]].rooms[self.playerLoc[0]].getBits()
                if currentRoomBits & 0b0001 == 0b0001 and currentLoc[0] in range(32*15,32*16) and currentLoc[1] == 32:
                    self.level.rows[self.playerLoc[1]].rooms[self.playerLoc[0]].setClear()
                    self.playerLoc=self.level.movePlayer([0,-1],self.playerLoc)
                    self.player.setPlayerLoc([496,17*32])
                    self.clearGroups()
                    self.getRoomContents(self.playerLoc,self.player)
                if currentRoomBits & 0b0010 == 0b0010 and currentLoc[0] in range(32*15,32*17) and currentLoc[1] in range(32*18,32*19):
                    self.level.rows[self.playerLoc[1]].rooms[self.playerLoc[0]].setClear()
                    self.playerLoc=self.level.movePlayer([0,1],self.playerLoc)
                    self.player.setPlayerLoc([496,2*32])
                    self.clearGroups()
                    self.getRoomContents(self.playerLoc,self.player)
                if currentRoomBits & 0b0100 == 0b0100 and currentLoc[0] == 960 and currentLoc[1] in range(32*9,32*11):
                    self.level.rows[self.playerLoc[1]].rooms[self.playerLoc[0]].setClear()
                    self.playerLoc=self.level.movePlayer([1,0],self.playerLoc)
                    self.player.setPlayerLoc([64,304])
                    self.clearGroups()
                    self.getRoomContents(self.playerLoc,self.player)
                if currentRoomBits & 0b1000 == 0b1000 and currentLoc[0] == 32 and currentLoc[1] in range(32*9,32*11):
                    self.level.rows[self.playerLoc[1]].rooms[self.playerLoc[0]].setClear()
                    self.playerLoc=self.level.movePlayer([-1,0],self.playerLoc)
                    self.player.setPlayerLoc([928,304])
                    self.clearGroups()
                    self.getRoomContents(self.playerLoc,self.player)
        if key[K_UP]:
            if self.player.checkOnBeat():
                self.addPlayerBullet(self.player.shoot([0,-1]))
        if key[K_DOWN]:
            if self.player.checkOnBeat():
                self.addPlayerBullet(self.player.shoot([0,1]))
        if key[K_LEFT]:
            if self.player.checkOnBeat():
                self.addPlayerBullet(self.player.shoot([-1,0]))
        if key[K_RIGHT]:
            if self.player.checkOnBeat() == True:
                self.addPlayerBullet(self.player.shoot([1,0]))

    def clearGroups(self):
        #empties all sprite groups
        self.enemies.empty()
        self.enemyBullets.empty()
        self.playerBullets.empty()
        self.items.empty()
        self.bosses.empty()

    def __onExit(self):
        pygame.quit()

    def mainMenu(self):
        #draws the main menu
        self.buttons=[]
        self.surface.fill((52,78,91))
        self.surface.blit(self.startButton,self.startButtonLoc)
        self.buttons.append(self.startButton)
        text("Welcome to Escape 3008!",self.font,(255,255,255),(50,80),self.surface)
        text("Use WASD to move around.",self.font,(255,255,255),(50,110),self.surface)
        text("Use arrow keys to attack.",self.font,(255,255,255),(50,140),self.surface)
        text("Use E to interact with doors.",self.font,(255,255,255),(50,170),self.surface)
        text("Press Esc to quit.",self.font,(255,255,255),(50,200),self.surface)
        pygame.display.flip()

    def getSeedMenu(self):
        #draws the menu and handles input of the seed used for random number generation
        nums=["0","1","2","3","4","5","6","7","8","9",]
        returning = False
        seedInput=""
        while returning == False:
            self.surface.fill((52,78,91))
            SeedInfo=text("Please type in your desired seed, or press enter to leave blank:",self.font,(255,255,255),(50,50),self.surface)
            playerInput=text(str(seedInput),self.font,(255,255,255),(50,100),self.surface)
            for key in pygame.event.get():
                if key.type == pygame.KEYDOWN:
                    if key.unicode in nums:
                        seedInput += key.unicode
                    elif key.unicode == "\b":
                        if len(seedInput)>0:
                            seedInput=seedInput.rstrip(seedInput[-1])
                    elif key.unicode == "\r":
                        returning = True
            pygame.display.flip()
        if seedInput == "":
            return None
        return int(seedInput)

    def mainGameInitialise(self):
        #loads the player
        self.player = player(2,10000,5,50,5,[self.playerCoords[0],self.playerCoords[1]],self.surface,self.playerBullets)

    def gameTurn(self):
        #handles the frame by fram running of the game
        #enemy movement, and collisions between objects
        toRemovePlayer=[]
        toRemoveEnemy=[]
        toRemoveItem=[]
        toAddBullets=[]
        toAddEnemies=[]
        #move and attack for each enemy
        for x in self.enemies.sprites():
            attack=x.takeTurn()
            if attack is not None:
                toAddBullets.append(attack)
        #move enemy bullets and check for player damage
        for x in self.enemyBullets.sprites():
            x.takeTurn()
            if x.checkCol(self.collider) == False:
                toRemoveEnemy.append(x)        
            if sprite.collide_rect(self.player,x) == True:
                x.doDamage(self.player)
                toRemoveEnemy.append(x)
        for x in self.bosses.sprites():
            hold=x.takeTurn()
            if hold is not None:
                for y in hold:
                    toAddEnemies.append(y)
        #move and check colls for player bullets
        for x in self.playerBullets.sprites():
            x.takeTurn()
            if x.checkCol(self.collider) == False:
                toRemovePlayer.append(x)
        #gets dict of all collisions between player bullets and enemies, then performs calcs
        if self.enemies:
            collisions=sprite.groupcollide(self.playerBullets,self.enemies,True,False)
            for x in collisions:
                x.doDamage(collisions[x][0])
        #collisions between player bullets and a boss
        if self.bosses:
            for x in self.playerBullets.sprites():
                boss=self.bosses.sprites()
                boss=boss[0]
                if sprite.collide_rect(boss,x) == True:
                    x.doDamage(boss)
                    toRemovePlayer.append(x)
        
        if len(self.items) > 0:
            for x in self.items.sprites():
                x.itemIdle(self.surface)
                if sprite.collide_rect(self.player,x) == True:
                    if type(x) == newFloor:
                        x.onPickup(self)
                    else:        
                        x.onPickup()
                        toRemoveItem.append(x)
        
        #deletes and adds bullets to sprite groups as necessary
        for x in toRemoveEnemy:
            self.enemyBullets.remove(x)   
        for x in toRemovePlayer:
            self.playerBullets.remove(x)
        for x in toRemoveItem:
            self.items.remove(x)
        for x in toAddBullets:
            self.addEnemyBullet(x)

        #checks for dead player and enemies
        if self.player.hp<=0:
            return True
        deadEnemies=[]
        deadBosses=[]
        for x in self.enemies:
            if x.hp<=0:
                self.player.gainScore(x.onDeath())
                deadEnemies.append(x)

        for x in self.bosses:
            if x.hp<=0:
                self.addItem(x.onDeath(self.tier,self.enemies,self.enemyBullets,self.bosses))
                deadBosses.append(x)

        for x in deadEnemies:
            self.enemies.remove(x)
        
        for x in deadBosses:
            self.bosses.remove(x)

    #the following addX functions all add objects to the requisite sprite group
    def addPlayerBullet(self,entity):
        self.playerBullets.add(entity)
    
    def addEnemyBullet(self,entity):
        self.enemyBullets.add(entity)

    def addEnemies(self,entities):
        for entity in entities:
            self.enemies.add(entity)
    
    def addItem(self,item):
        self.items.add(item)

    def getRoomContents(self,roomCoords,player):
        contents=None
        room=self.level.rows[roomCoords[1]].rooms[roomCoords[0]]
        type=room.getType()
        if type != "Start":
            self.level.loadRoomContents(roomCoords,player)
            if type.lower() == "standard":
                contents = room.getEnemies()
                if contents != None:
                    self.addEnemies(contents)
            elif type.lower() =="treasure room":
                contents = room.getTreasure()
                if contents != None:
                    self.addItem(contents)
            elif type.lower() =="boss room":
                if room.isClear() == True:
                    self.addItem(newFloor("nextLevel",self.player,(0,0,0),self.tier+1,self.enemies,self.enemyBullets,self.bosses))

    def mainGame(self):
        #draws the room and gets the results of the current frame
        self.surface.blit(self.possibleRooms[self.level.rows[self.playerLoc[1]].rooms[self.playerLoc[0]].getBits()],(0,0))
        self.player.playerIdle()
        return self.gameTurn()

    def on_execute(self):
        #handles the core running of the game engine
        self.__on_init()
        while(self._running):
        ###game loop is here###
            while self.inMainMenu == True:
                self.mainMenu()
                for event in pygame.event.get():
                    self.__on_event_menu(event)
            if self.inMainGame == True:
                self.mainGameInitialise()
            while self.inMainGame == True:
                isDead=self.mainGame()
                keys = key.get_pressed() 
                self.gameKeyManager(keys)
                for event in pygame.event.get():
                    self.__on_event_game(event)
                if self._running == True:
                    self.__displayUI()
                    display.flip()
                if isDead:
                    self.inMainGame=False
                    self.inMainMenu=True
            self.clearGroups()
        self.__onExit()
        
    def loadLevel(self,roomsX,roomsY,numRooms,tier,isFirst):
        #creates the level
        self.level=BuildLevel1(roomsX,roomsY,numRooms,self.seed,tier,self.surface,self.enemies,self.enemyBullets,self.bosses).getLevel()
        self.playerLoc=self.level.getStart()
        self.level.visualiseLevel()
        if isFirst:
            #if this is the first level created makes all possible rooms
            self.__loadRoomImgs()
        
    def __loadRoomImgs(self):
        #creates images for all possible rooms
        floorMap=tilemap(self.resource_path("Assets\\Environments\\SpaceStationTileset.png"),32)
        wallMap=tilemap(self.resource_path("Assets\\Environments\\housetileset.png"),32)
        dummyRooms=[Room(0,0,0,1,0,"Standard"),Room(0,0,1,0,0,"Standard"),Room(0,1,0,0,0,"Standard"),Room(1,0,0,0,0,"Standard"),Room(1,1,0,0,0,"Standard"),Room(0,1,1,0,0,"Standard"),Room(0,0,1,1,0,"Standard"),Room(1,0,1,0,0,"Standard"),Room(0,1,0,1,0,"Standard"),Room(1,0,0,1,0,"Standard"),Room(1,1,1,0,0,"Standard"),Room(0,1,1,1,0,"Standard"),Room(1,1,0,1,0,"Standard"),Room(1,0,1,1,0,"Standard"),Room(1,1,1,1,0,"Standard")]
        for x in range(len(dummyRooms)):
            dummyRooms[x].generateBits()
        for x in range(len(dummyRooms)):    
            currentBits=dummyRooms[x].getBits()
            toAdd=drawRoom(dummyRooms[x],self.size,floorMap,wallMap).generateImage()
            self.possibleRooms[currentBits]=toAdd
        print("Made room images")

    def __displayUI(self):
        #draws the player UI with stats
        text(f"Health = {str(self.player.getHp())}",self.uiFont,(255,255,255),(20,0),self.surface)
        text(f"Attack power = {str(self.player.getAtk())}",self.uiFont,(255,255,255),(150,0),self.surface)
        text(f"Score = {str(self.player.getScore())}",self.uiFont,(255,255,255),(320,0),self.surface)
    
    def __loadImages(self):
        #loads the button image
        buttonPath=self.resource_path("Assets\\UI_elements\\RetroWindowsGUI\\Windows_Button.png")
        self.startButton=button("To start, press space",buttonPath,5,200,25,self.startButtonLoc).makeButton()

    def resource_path(self, relative_path):
        #get absolute path to resource, works for dev and for PyInstaller
        #used in creation of .exe file
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
if __name__ == "__main__":
    game=Escape3008()
    game.on_execute()
