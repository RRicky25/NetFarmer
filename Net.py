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

    def draw(self,win,camX,camY):
        self.rect.x-=camX
        self.rect.y-=camY
        pygame.draw.rect(win,(0,255,255),self.rect)
        self.rect.x+=camX
        self.rect.y+=camY
    
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        if self.rect.x>self.WIDTH or self.rect.x<0:
            self.kill()
            return
        if self.rect.y>self.HEIGHT or self.rect.y<0:
            self.kill()
            return
        self.check_collision()
    
    #check for collision with level in case of colision destory it and return true
    def check_collision(self):
        pos=[self.rect.x*64//self.WIDTH,self.rect.y*64//self.WIDTH]
        blocks=self.level.returnBlocks(pos)
        hit_list=[]
        for block in blocks:
            if self.rect.colliderect(block):
                hit_list.append(block)
        
        if len(hit_list)>0:
            self.kill()
    #called when the class is deleted
    