#Various classes used in the running of the game
from pygame import *
from mapGen import *
import random
import os
init()

class text:
    #class to draw text
    def __init__(self,text,font,colour,coords,surface):
        self.position=coords
        self.text=text
        self.font=font
        self.colour=colour
        self.surface=surface
        self.drawText()
        
    def drawText(self):
        text=self.font.render(self.text, True, self.colour)
        self.surface.blit(text, self.position)

class drawRoom():
    #class to generate an image for a room with specified connections
    def __init__(self,room,windowSize,floorImg,wallImg):
        self.room = room
        self.bits = self.room.getBits()
        self.roomSize = windowSize
        self.screen = Surface(windowSize)
        self.width = windowSize[0]
        self.height = windowSize[1]
        self.tileSize = 32
        #both tilesets used have a size of 32 pixels
        self.floorMap = floorImg
        self.wallMap = wallImg
        self.getTiles()

    def getTiles(self):
        #loads the individual tiles used to make the rooms
        #corners
        self.UCornerL=self.wallMap.getTile(5*32,7*32)
        self.UCornerR=self.wallMap.getTile(7*32,7*32)
        self.LCornerL=self.wallMap.getTile(5*32,9*32)
        self.LCornerR=self.wallMap.getTile(7*32,9*32)
        #walls
        self.backWallImg1=self.wallMap.getTile(6*32,8*32)
        self.backWallImg2=self.wallMap.getTile(6*32,6*32)
        self.sideWallImgL=self.wallMap.getTile(5*32,7*32)
        self.sideWallImgR=self.wallMap.getTile(7*32,7*32)
        self.bottomWallImg=self.wallMap.getTile(6*32,9*32)
        #floor
        self.floorImg1=self.floorMap.getTile(19*32,24*32)
        self.floorImg2=self.floorMap.getTile(18*32,24*32)
        #doors
        self.doorImgHoriz=self.floorMap.getTile(10*32,17*32)
        self.doorImgHoriz2=self.floorMap.getTile(11*32,17*32)
        self.doorImgVert=self.floorMap.getTile(12*32,20*32)
        self.doorImgVert2=self.floorMap.getTile(12*32,21*32)

    def testTiles(self):
        #Debugging, used to check each image is being correctly loaded
        #corners
        self.screen.blit(self.UCornerL,(0,0))
        self.screen.blit(self.UCornerR,(self.width-self.tileSize,0))
        self.screen.blit(self.LCornerL,(0,self.height-self.tileSize))
        self.screen.blit(self.LCornerR,(self.width-self.tileSize,self.height-self.tileSize))
        #walls
        self.screen.blit(self.sideWallImgL,(0,self.height/2))
        self.screen.blit(self.backWallImg,(self.width/2,0))
        self.screen.blit(self.sideWallImgR,(0,self.height/2))
        self.screen.blit(self.bottomWallImg,(self.width/2,self.height-self.tileSize))
        #floor
        self.screen.blit(self.floorImg1,(self.width/2,self.height/2))
        return self.screen

    def generateImage(self):
        #places the tiles onto the image
        currentLoc=[0,0]
        num=2
        for x in range(int((self.width*self.height)/self.tileSize)):
            #If first get tile 0, if still on top row get tile 1, if end of top row get tile 2, etc
            #self.button.blit(rects[x],(currentLoc[0],currentLoc[1]))

            if currentLoc[0] != self.width:
                if currentLoc[0]==0 and currentLoc[1]==0:
                    self.screen.blit(self.UCornerL,(currentLoc[0],currentLoc[1]))

                elif currentLoc[0] == self.width-self.tileSize and currentLoc[1]==0:
                    self.screen.blit(self.UCornerR,(currentLoc[0],currentLoc[1]))
                    
                elif currentLoc[0]<self.width-self.tileSize and currentLoc[1]==0:
                    if num%2==0:
                        self.screen.blit(self.backWallImg1,(currentLoc[0],currentLoc[1]))
                    else:
                        self.screen.blit(self.backWallImg2,(currentLoc[0],currentLoc[1]))
                    num+=1

                elif currentLoc[0]==0 and currentLoc[1]!= 0 and currentLoc[1]<self.height-self.tileSize:
                    
                    self.screen.blit(self.sideWallImgL,(currentLoc[0],currentLoc[1]))

                elif currentLoc[0]<self.width-self.tileSize and currentLoc[1]!=0 and currentLoc[1]<self.height-self.tileSize:
                    num=random.randint(1,2)
                    if num == 1:
                        self.screen.blit(self.floorImg1,(currentLoc[0],currentLoc[1]))
                    else:
                        self.screen.blit(self.floorImg2,(currentLoc[0],currentLoc[1]))
                    
                elif currentLoc[0]==self.width-self.tileSize and currentLoc[1]!=self.height-self.tileSize:
                    self.screen.blit(self.sideWallImgR,(currentLoc[0],currentLoc[1]))
                    
                elif currentLoc[0]==0 and currentLoc[1]==self.height-self.tileSize:
                    #replace with bottom left corner
                    self.screen.blit(self.LCornerL,(currentLoc[0],currentLoc[1]))
                    
                elif currentLoc[0]<self.width-self.tileSize and currentLoc[1]==self.height-self.tileSize:
                    self.screen.blit(self.bottomWallImg,(currentLoc[0],currentLoc[1]))
                    
                elif currentLoc[0]==self.width-self.tileSize and currentLoc[1]==self.height-self.tileSize:
                    #replace with bottom right corner
                    self.screen.blit(self.LCornerR,(currentLoc[0],currentLoc[1]))
                currentLoc[0]+=self.tileSize
            else:
                currentLoc[0]=0
                currentLoc[1]+=self.tileSize
        self.placeDoorways()
        return self.screen
    
    def placeDoorways(self):
        #adds the doorway images to the room
        if self.bits & 0b0001 == 0b0001:
            self.screen.blit(self.doorImgHoriz,(self.width/2-self.tileSize,0))
            self.screen.blit(self.doorImgHoriz2,(self.width/2,0))
        if self.bits & 0b0010 == 0b0010:
            self.screen.blit(self.doorImgHoriz,(self.width/2-self.tileSize,self.height-self.tileSize))
            self.screen.blit(self.doorImgHoriz2,(self.width/2,self.height-self.tileSize))
        if self.bits & 0b0100 == 0b0100:
            self.screen.blit(self.doorImgVert,(self.width-self.tileSize,self.height/2-self.tileSize))
            self.screen.blit(self.doorImgVert2,(self.width-self.tileSize,self.height/2))
        if self.bits & 0b1000 == 0b1000:
            self.screen.blit(self.doorImgVert,(0,self.height/2-self.tileSize))
            self.screen.blit(self.doorImgVert2,(0,self.height/2))
            
                    
class button():
    #way to display text with a button-style background
    #start and end tile should be rects
    #height and width should be divisible by the tilesize of the tilemap
    def __init__(self,text,img,tileSize,buttonWidth,buttonHeight,location):
        self.text=text
        self.font=font.SysFont("alegria",30)
        self.height=int(buttonHeight)
        self.width=int(buttonWidth)
        self.button=Surface((self.width,self.height))
        self.tileSize=tileSize
        self.img=tilemap(img,tileSize)
        self.hitBox=Rect((location[0],location[1]),(int(buttonHeight),int(buttonWidth)))

    def generateRects(self):
        #first rect will always be for the top left, last rect will always be bottom right
        rects=[]
        currentLoc=[0,0]
        #currently needs to be specified for source width and height
        for x in range(9):
            toAdd=Rect(currentLoc[0],currentLoc[1],self.tileSize,self.tileSize)
            rects.append(toAdd)
            if currentLoc[0] != 10:
                currentLoc[0]+=self.tileSize
            else:
                currentLoc[0]=0
                currentLoc[1]+=self.tileSize
        return rects

    def getImgs(self):
        rects=self.generateRects()
        return self.img.getTiles(rects)

    def makeButton(self):
        currentLoc=[0,0]
        rects=self.getImgs()
        for x in range(int(self.width*self.height/self.tileSize)):
            if currentLoc[0] != self.width:
                if currentLoc[0]==0 and currentLoc[1]==0:
                    self.button.blit(rects[0],(currentLoc[0],currentLoc[1]))
                elif currentLoc[0]<self.width-self.tileSize and currentLoc[1]==0:
                    self.button.blit(rects[1],(currentLoc[0],currentLoc[1]))
                elif currentLoc[0]==self.width-self.tileSize and currentLoc[1]==0:
                    self.button.blit(rects[2],(currentLoc[0],currentLoc[1]))
                elif currentLoc[0]==0 and currentLoc[1]!= 0 and currentLoc[1]<self.height-self.tileSize:
                    self.button.blit(rects[3],(currentLoc[0],currentLoc[1]))
                elif currentLoc[0]<self.width-self.tileSize and currentLoc[1]!=0 and currentLoc[1]<self.height-self.tileSize:
                    self.button.blit(rects[4],(currentLoc[0],currentLoc[1]))
                elif currentLoc[0]==self.width-self.tileSize and currentLoc[1]<self.height-self.tileSize:
                    self.button.blit(rects[5],(currentLoc[0],currentLoc[1]))
                elif currentLoc[0]==0 and currentLoc[1]==self.height-self.tileSize:
                    self.button.blit(rects[6],(currentLoc[0],currentLoc[1]))
                elif currentLoc[0]<self.width-self.tileSize and currentLoc[1]==self.height-self.tileSize:
                    self.button.blit(rects[7],(currentLoc[0],currentLoc[1]))
                elif currentLoc[0]==self.width-self.tileSize and currentLoc[1]==self.height-self.tileSize:
                    self.button.blit(rects[8],(currentLoc[0],currentLoc[1]))
                currentLoc[0]+=self.tileSize
            else:
                currentLoc[0]=0
                currentLoc[1]+=self.tileSize
        buttonText=text(self.text,self.font,(0,0,0),(0,0),self.button)
        return self.button

class tilemap:
    #loads a tilemap and silces it into specified tile sizes
    def __init__(self,img,tileSize):
        self.img=image.load(img).convert_alpha()
        self.size=tileSize
        
    def getTile(self,rectX,rectY):
        #gets the tile at the specified coordinate
        toGet=Rect(rectX,rectY,self.size,self.size)
        imgToReturn=Surface(toGet.size).convert()
        imgToReturn.blit(self.img,(0,0),toGet)
        return imgToReturn
    
    def getTiles(self,rects):
        #gets a list of tiles at specified coordinates
        imgs=[]
        for x in range(len(rects)):
            imgs.append(self.getTile(rects[x][0],rects[x][1]))
        return imgs