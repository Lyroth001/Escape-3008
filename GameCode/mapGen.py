import random
import items
from enemy import *
from bosses import *
class Room:
    def __init__(self,n,s,e,w,p,name):
        self.n=n
        self.s=s
        self.e=e
        self.w=w
        self.isPlayer=p
        self.name=name
        self.cleared=False
        self.enemies=None
        self.northConnection = "┴" if self.n == 1 else "─"
        self.eastConnection = "├" if self.e == 1 else "│"
        self.southConnection = "┬" if self.s == 1 else "─"
        self.westConnection = "┤" if self.w == 1 else "│"
        self.player = "P" if self.isPlayer == 1 else " "
        self.drawOptions=[f"┌─{self.northConnection}─┐","│   │",f"{self.westConnection} {self.player} {self.eastConnection}",f"│   │",f"└─{self.southConnection}─┘"]
            
    def playerEnter(self):
        self.isPlayer = 1
        self.player = "P"
        self.drawOptions=[f"┌─{self.northConnection}─┐","│   │",f"{self.westConnection} {self.player} {self.eastConnection}",f"│   │",f"└─{self.southConnection}─┘"]

    def playerExit(self):
        self.isPlayer = 0
        self.player = " "
        self.drawOptions=[f"┌─{self.northConnection}─┐","│   │",f"{self.westConnection} {self.player} {self.eastConnection}",f"│   │",f"└─{self.southConnection}─┘"]

    def generateBits(self):
        self.bitVal=0b0000
        if self.n==1:
            self.bitVal+=0b0001
        if self.s==1:
            self.bitVal+=0b0010
        if self.e==1:
            self.bitVal+=0b0100
        if self.w==1:
            self.bitVal+=0b1000
    
    def isClear(self):
        return self.cleared
    
    def setClear(self):
        self.cleared=True
        self.enemies=None
        
    def getBits(self):
        return self.bitVal
        
    def debugGetContentsAsList(self):
        #Mainly for debugging
        return [self.n, self.s, self.e, self.w, self.isPlayer,self.name]

    def getType(self):
        return str(self.name)

    def update(self,n,s,e,w,p,name):
        #enables data to be toggled
        self.n=n
        self.s=s
        self.e=e
        self.w=w
        self.isPlayer=p
        self.name=name
        self.northConnection = "┴" if self.n == 1 else "─"
        self.eastConnection = "├" if self.e == 1 else "│"
        self.southConnection = "┬" if self.s == 1 else "─"
        self.westConnection = "┤" if self.w == 1 else "│"
        self.player = "P" if self.isPlayer == 1 else " "
        self.drawOptions=[f"┌─{self.northConnection}─┐","│   │",f"{self.westConnection} {self.player} {self.eastConnection}",f"│   │",f"└─{self.southConnection}─┘"]

    def setEnemies(self,enemies):
        self.enemies=enemies
    
    def getEnemies(self):
        print(self.cleared)
        if self.cleared==False:
            return self.enemies
        else:
            return None

    def print(self):
        #print(self.name, end="")
        print(f"┌─{self.northConnection}─┐\n│   │\n{self.westConnection} {self.player} {self.eastConnection}\n│   │\n└─{self.southConnection}─┘",end="")
        
    def printPart(self,toPrint,isEnd):
        if isEnd == False:
            print(self.drawOptions[toPrint],end="")
        else:
            print(self.drawOptions[toPrint]+"\n",end="")

class SymbolRoom(Room):
    def __init__(self,n,s,e,w,p,name,symbol):
        super().__init__(n,s,e,w,p,name)
        self.symbol=symbol
        self.drawOptions=[f"┌─{self.northConnection}─┐",f"│{self.symbol}  │",f"{self.westConnection} {self.player} {self.eastConnection}",f"│   │",f"└─{self.southConnection}─┘"]

    def getItem(self):
        return self.item

    def getSymbol(self):
        return self.symbol

    def playerEnter(self):
        self.isPlayer = 1
        self.player = "P"
        self.drawOptions=[f"┌─{self.northConnection}─┐",f"│{self.symbol}  │",f"{self.westConnection} {self.player} {self.eastConnection}",f"│   │",f"└─{self.southConnection}─┘"]

    def playerExit(self):
        self.isPlayer = 0
        self.player = " "
        self.drawOptions=[f"┌─{self.northConnection}─┐",f"│{self.symbol}  │",f"{self.westConnection} {self.player} {self.eastConnection}",f"│   │",f"└─{self.southConnection}─┘"]

    def update(self,n,s,e,w,p,name,symbol):
        super().update(n,s,e,w,p,name)
        self.symbol=symbol
        self.drawOptions=[f"┌─{self.northConnection}─┐",f"│{self.symbol}  │",f"{self.westConnection} {self.player} {self.eastConnection}",f"│   │",f"└─{self.southConnection}─┘"]

    def print(self):
        #print(self.name,end="")
        print(f"┌─{self.northConnection}─┐\n│{self.symbol}   │\n{self.westConnection} {self.player} {self.eastConnection}\n│  {self.item}│\n└─{self.southConnection}─┘",end="")

        
class TreasureRoom(SymbolRoom):
    def __init__(self,n,s,e,w,p,name,item,symbol):
        super().__init__(n,s,e,w,p,name,symbol)
        self.item=item

    def update(self,n,s,e,w,p,name,item,symbol):
        super().update(n,s,e,w,p,name,symbol)
        self.item=item

    def getTreasure(self):
        return self.item    

    def setItem(self,item):
        self.item=item
    
class BossRoom(SymbolRoom):
    def __init__(self,n,s,e,w,p,name,symbol):
        super().__init__(n,s,e,w,p,name,symbol)

    def update(self,n,s,e,w,p,name,symbol):
        super().update(n,s,e,w,p,name,symbol)

    def setBoss(self,boss):
        self.boss=boss
        
    def foughtBoss(self):
        #completes level, moves to next
        pass
    
    def getBoss(self):
        return self.boss
    
class Level:
    def __init__(self,rows,tier=0):
        self.rows=rows
        self.tier=tier

    def setTier(self,tier):
        self.tier=tier

    def getTier(self):
        return self.tier

    def debugGetContentsAsList(self):
        for x in range(0,len(self.rows)):
            print(self.rows[x].debugGetContentsAsList())

    def getStart(self):
        for y in range(0,len(self.rows)):
            for x in range(0,len(self.rows[y].rooms)-1):
                if self.rows[y].rooms[x].name.lower()=="start":
                    return [x,y]
                
    def visualiseLevel(self):
        for x in range(0,len(self.rows)):
            self.rows[x].visualiseRow()
            
    def movePlayer(self, direction,currentLocation):
        try:
            newLocation=[0,0]
            success=False
            newLocation[1]=currentLocation[1]+direction[1]
            newLocation[0]=currentLocation[0]+direction[0]
            if self.rows[newLocation[1]].rooms[newLocation[0]].name != "":
                self.rows[currentLocation[1]].rooms[currentLocation[0]].playerExit()
                self.rows[newLocation[1]].rooms[newLocation[0]].playerEnter()
                success=True
            if success==True:
                return newLocation
            else:
                return currentLocation
        except:
            print("Please enter a valid movement (i.e. into a room that exists)")

    def getPlayerLocation(self):
        for y in range(0,len(self.rows)):
            for x in range(0,len(self.rows[y].rooms)-1):
                if self.rows[y].rooms[x].isPlayer==1:
                    return [x,y]

    def setBosses(self,bossList):
        self.bosses=bossList

    def setEnemies(self,enemyList):
        self.enemies = enemyList
                
    def loadRoomContents(self,currentRoom,player):
        currentRoom=self.rows[currentRoom[1]].rooms[currentRoom[0]]
        if currentRoom.isClear() == False:
            if currentRoom.getType() == "Treasure room":
                #spawn item
                currentRoom.setItem(items.assignItem(player,self.tier))

            elif currentRoom.getType() == "Boss room":
                #spawn boss
                print("boss room")
                thisBoss=self.bosses[random.randint(0,len(self.bosses)-1)]
                if thisBoss["name"]=="Doctor":
                    toAdd=doctor(thisBoss["hp"],thisBoss["atkpwr"],thisBoss["atkspd"],thisBoss["movspd"],thisBoss["name"],thisBoss["screen"],thisBoss["bossGroup"],thisBoss["bulletGroup"],score=thisBoss["score"])
                toAdd.bossInit(player)
                currentRoom.setBoss(thisBoss)
                
            elif currentRoom.getType() == "Standard":
                enemyNum=random.randint(2,10)
                enemies=[]
                for x in range(enemyNum):
                    toAdd=self.buildEnemy()
                    enemies.append(toAdd)
                for y in enemies:
                    y.enemyInit(player)
                currentRoom.setEnemies(enemies)

    def buildEnemy(self):
        enemyToUse=random.randint(0,len(self.enemies)-1)
        enemyData=self.enemies[enemyToUse]
        if enemyData["name"] == "enemy":
            newEnemy = enemy(enemyData["hp"],enemyData["atkpwr"],enemyData["atkspd"],enemyData["movspd"],enemyData["colour"],enemyData["name"],enemyData["screen"],enemyData["enemyGroup"],enemyData["bulletGroup"],enemyData["score"])
        return newEnemy
class Row:
    def __init__(self,rooms):
        self.rooms=rooms
        
    def debugGetContentsAsList(self):
        #Mainly for debugging
        contents=[]
        for x in range(0,len(self.rooms)):
            contents.append(self.rooms[x].debugGetContentsAsList())
        return contents

    def getRoom(self,roomIndex):
        return self.rooms[roomIndex]
    
    def changeRoom(self,roomToChange,newData):
        #replaces room with other room
        self.rooms[roomToChange]=newData

    def visualiseRow(self):
        for x in range(0,len(self.rooms[0].drawOptions)):
            for y in range(0,len(self.rooms)):
                if y == len(self.rooms)-1:
                    self.rooms[y].printPart(x,True)
                else:
                    self.rooms[y].printPart(x,False)


class BuildFloorInterface:
    def __init__(self,x,y,rooms,tier,seed=None):
        if seed is None:
            seed = random.randint(0,9999999999999999)
        print(f"seed = {seed}")
        random.seed(seed)
        self.tier=tier
        self.numRooms=x
        self.numRows=y
        self.maxRooms=rooms
        self.directions=[[0,-1],[0,1],[1,0],[-1,0]]
        self.floorPlan=self.__createPathStartToBoss()
        self.printMap()

    def getLevel(self):
        return self.floorPlan
        
    def __generateMap(self):
        #Creates a map object with empty rooms
        output = None
        print("Generating shell...")
        plan=[]
        for y in range(0,self.numRows):
            blueprint=[]
            for x in range(0,self.numRooms):
                name = ""
                n=0
                s=0
                e=0
                w=0
                p=0 
                if x == 0 and y == 0:
                    name = "Start"
                    # TODO: Drive Connections?
                    s=1
                    e=1
                    p=1
                room = Room(n, s, e , w, p, name)
                blueprint.append(room)
            plan.append(Row(blueprint))
        output=Level(plan)
        #startRoom=Room(0,0,0,0,1,"Cafe")
        #output.rows[2].changeRoom(0,startRoom)
        #Use cafe later for health pickups?
        return output

    def __updateConnections(self,level):
        #Updates connections between rooms in the completed map
        for y in range(0,len(level.rows)):
            for x in range(0,len(level.rows[y].rooms)):
                connections=[]
                room=level.rows[y].rooms[x]
                roomType=room.getType()
                if roomType != "":
                    for z in range(0,len(self.directions)):
                        if self.__checkRoomInBound([x,y],self.directions[z]) == True:
                            nearRoom=level.rows[y+self.directions[z][1]].getRoom(x+self.directions[z][0])
                            if nearRoom.getType() != "":
                                connections.append(1)
                            else:
                                connections.append(0)
                        else:
                            connections.append(0)
                    if roomType != "Standard" and roomType != "Start":
                        if roomType == "Boss room":
                            level.rows[y].rooms[x].update(connections[0],connections[1],connections[2],connections[3],room.isPlayer,roomType,room.getSymbol())
                        if roomType == "Treasure room":
                            level.rows[y].rooms[x].update(connections[0],connections[1],connections[2],connections[3],room.isPlayer,roomType,room.getItem(),room.getSymbol())
                    else:
                        level.rows[y].rooms[x].update(connections[0],connections[1],connections[2],connections[3],room.isPlayer,roomType)
        return level
                        
    def __generateBits(self, level):
        for y in range(0,len(level.rows)):
            for x in range(0,len(level.rows[y].rooms)):
                level.rows[y].rooms[x].generateBits()
        return level

    def __createLevel(self):
        #builds a level object and places a boss room
        level=self.__generateMap()
        level=self.__selectBossRoom(level)
        return level

    def __getRandomCoord(self):
        coord=[]
        coord.append(random.randint(0,self.numRooms-1))
        coord.append(random.randint(0,self.numRows-1))
        return coord
    
    def __selectBossRoom(self,level):
        print("Placing boss...")
        coord=self.__getRandomCoord()
        level.rows[coord[1]].changeRoom(coord[0],BossRoom(0,0,0,0,0,"Boss room","x"))
        return level

    def __checkRoomInBound(self,roomCoords,direction):
        #prevents program from erroring out by checking if a room intended to be accessed would be within the bounds of the map (prevents index error)
        if roomCoords[0]+direction[0]>-1 and roomCoords[1]+direction[1]<= self.numRows-1 and roomCoords[0]+direction[0]<=self.numRooms-1 and roomCoords[1]+direction[1]>=0:
            return True
        else:
            return False
        
    def __createRoomNeighbour(self,level,roomCoords,direction):
        try:
            if self.__checkRoomInBound(roomCoords,direction) == True:
                if level.rows[roomCoords[1]+direction[1]].rooms[roomCoords[0]+direction[0]].name=="":
                    level.rows[roomCoords[1]+direction[1]].changeRoom(roomCoords[0]+direction[0],Room(0,0,0,0,0,"Standard"))
                    roomCoords[0]=roomCoords[0]+direction[0]
                    roomCoords[1]=roomCoords[1]+direction[1]
                else:
                    return False
                return [True,level,roomCoords]
            else:
                return False
        except:
            return False

    def __getMove(self):
        selected=random.randint(0,3)
        return self.directions[selected]

    def __checkPathToBoss(self,level):
        #checks if there is a path between the boss room and the start room
        currentRoom=level.getStart()
        move=self.__getMove()
        finished=False
        valid=False
        print("Checking path...")
        attempts=0
        try:
            while finished == False:
                #checks move is valid
                if self.__checkRoomInBound(currentRoom,move) == True:
                    #checks move leads to room and not empty
                    if level.rows[currentRoom[1]+move[1]].rooms[currentRoom[0]+move[0]].getType() != "":
                        #moves pointer into room
                        currentRoom=[currentRoom[0]+move[0],currentRoom[1]+move[1]]
                        #checks if room is boss and if so, ends loop
                        if level.rows[currentRoom[1]].rooms[currentRoom[0]].name == "Boss room":
                            finished=True
                            valid=True
                            print("Path success")
                            return valid
                        attempts=0                          
                else:
                    finished = False
                attempts += 1
                if attempts > 3:
                    print("Path failed")
                    return False
                move=self.__getMove()
            return valid
        except:
            print("Could not check path")
            return False
   
    def __createPathStartToBoss(self):
        #creates a level with rooms connecting the start room and boss room
        #creates potential levels until one is found with proper connections, trying a maximum of 100 times
        attempts=0
        successful=False
        currentRoom=None
        while successful == False:
            level=self.__createLevel()
            currentRoom=level.getStart()
            roomCount=0
            saved=0
            print("Creating path...")
            while roomCount < self.maxRooms:
                possible=False
                tryPlaceRoom=0
                while possible==False:
                    output=self.__createRoomNeighbour(level,currentRoom,self.__getMove())
                    if str(type(output)) != "<class 'list'>":
                        possible=False
                        tryPlaceRoom+=1
                        if tryPlaceRoom >= 30:
                            break
                    else:
                        possible=output[0]
                        level=output[1]
                        currentRoom=output[2]
                        roomCount += 1
                    if tryPlaceRoom >= 30:
                        break
                if tryPlaceRoom >= 30:
                        break
            attempts += 1
            try:
                successful=self.__checkPathToBoss(level)
            except:
                successful=False
            print(f"attempts = {attempts}")
            print(f"room count = {roomCount}")
            if attempts > 100:
                print("couldn't build map successfully :(")
                input()
                exit()
        print("Placing treasure...")
        level=self.__placeTreasureRoom(level)
        print("Updating connections...")
        level=self.__updateConnections(level)
        print("Generating Bits")
        level=self.__generateBits(level)
        print("Returning...")
        level.setTier(self.tier)
        return level

    def __placeTreasureRoom(self, level):
        placed = False
        while placed == False:
            coord=self.__getRandomCoord()
            if level.rows[coord[1]].rooms[coord[0]].getType() == "Standard":
                try:
                    toAdd=TreasureRoom(0,0,0,0,0, "Treasure room", "Coin", "G")
                    level.rows[coord[1]].changeRoom(coord[0],toAdd)
                    return level
                    placed = True
                except:
                    placed = False
                        
    def printMap(self):
        #outputs the visual map of a level
        for x in range(0,len(self.floorPlan.rows)):
            print(self.floorPlan.rows[x].debugGetContentsAsList())