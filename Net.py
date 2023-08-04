import pygame
class Net(pygame.sprite.Sprite):
    def __init__(self,W,H,x,y,velx,vely,width,height,level):
        super().__init__()
        self.x,self.y=x,y
        self.velx,self.vely=velx,vely
        self.rect=pygame.Rect(self.x,self.y,width,height)
        self.WIDTH=W
        self.HEIGHT=H
        self.level=level

    def draw(self,win):
        print(self.rect)
        pygame.draw.rect(win,(0,255,255),self.rect)
    
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        if self.rect.x>self.WIDTH or self.rect.x<0:
            print("Exceeded")
            self.kill()
            return
        if self.rect.y>self.HEIGHT or self.rect.y<0:
            self.kill()
            return
        self.check_collision(self.level)
    
    #check for collision with level in case of colision destory it and return true
    def check_collision(self,level):
        pos=[self.rect.x//self.WIDTH,self.rect.y//self.WIDTH]
        blocks=self.returnBlocks(pos)
        hit_list=[]
        for block in blocks:
            if self.rect.colliderect(block):
                hit_list.append(block)
        if hit_list:
            print("Killed in action")
            self.kill()
    
    def returnBlocks(self,pos):
        blocks=[]
        for i in range(pos[1]-1,pos[1]+5):
            for j in range(pos[0]-1,pos[0]+5):
                try:
                    if self.level.level[i][j]==self.level.legend["land"]:
                        blocks.append(pygame.Rect(j*self.WIDTH,i*self.WIDTH,self.WIDTH,self.WIDTH))
                except:
                    pass
        return blocks
    
    #called when the class is deleted