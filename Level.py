import pickle
import pygame

class Level:
    #load level from src
    def __init__(self,WIDTH,src):
        self.level=pickle.load(open(src,"rb"))
        self.width=len(self.level[0])
        self.height=len(self.level)
        self.legend={"land":1,"air":0,"plant":2}
        self.WIDTH=WIDTH
    
    #draw on the win
    def draw(self,win):
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j]==1:
                    pygame.draw.rect(win, (255, 0, 0), (j*self.WIDTH, i*self.WIDTH, self.WIDTH, self.WIDTH))
    
    #return random plant
    def random_plant():
        pass
    
    def returnBlocks(self,pos):
        blocks=[]
        for i in range(pos[1]-1,pos[1]+5):
            for j in range(pos[0]-1,pos[0]+5):
                try:
                    if self.level[i][j]==self.legend["land"]:
                        blocks.append(pygame.Rect(j*self.WIDTH,i*self.WIDTH,self.WIDTH,self.WIDTH))
                except:
                    pass
        return blocks
    
