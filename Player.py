import pygame
from Net import *
class Player:
    def __init__(self,x,y,width,height,WIDTH,level):
        self.x,self.y,self.width,self.height=x,y,width,height
        self.vel=[0,0]
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.y_momentum=0
        self.air_timer=0
        self.n_jumps=0
        self.WIDTH=WIDTH
        self.level=level
    
    def draw(self,win):
        # win.blit(robot, (self.rect.x - camX - 15, self.rect.y - camY - 15))
        pygame.draw.rect(win,(0,0,255),self.rect)

    def physics(self):
        self.vel=[0,0]
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.vel[0]-=self.WIDTH/3
        if key[pygame.K_RIGHT]:
            self.vel[0]+=self.WIDTH/3
        if key[pygame.K_UP] and self.air_timer<3:
            if self.air_timer==1:
                self.n_jumps+=1
            self.y_momentum=-self.WIDTH
        elif key[pygame.K_UP] and self.air_timer>20 and self.n_jumps<2:
            self.n_jumps+=1
            self.air_timer=0
            self.y_momentum=-self.WIDTH
        self.vel[1]+=self.y_momentum
        self.y_momentum+=self.WIDTH/15
        if self.y_momentum>self.WIDTH:
            self.y_momentum=self.WIDTH
        collisions=self.move()
        if collisions['bottom']:
            self.y_momentum = 0
            self.air_timer = 0
            self.n_jumps=0
        else:
            self.air_timer += 1
    
    def move(self):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.rect.x+=self.vel[0]
        pos=[self.rect.x//self.WIDTH,self.rect.y//self.WIDTH]
        blocks=self.level.returnBlocks(pos)
        hit_list=[]
        for block in blocks:
            if self.rect.colliderect(block):
                hit_list.append(block)
        for tile in hit_list:
            if self.vel[0] > 0:
                self.rect.right = tile.left
                collision_types['right'] = True
            elif self.vel[0] < 0:
                self.rect.left = tile.right
                collision_types['left'] = True
        
        self.rect.y+=self.vel[1]
        pos=[self.rect.x//self.WIDTH,self.rect.y//self.WIDTH]
        blocks=self.level.returnBlocks(pos)
        hit_list=[]
        for block in blocks:
            if self.rect.colliderect(block):
                hit_list.append(block)

        for tile in hit_list:
            if self.vel[1] > 0:
                self.rect.bottom = tile.top
                collision_types['bottom'] = True
            elif self.vel[1] < 0:
                self.rect.top = tile.bottom
                collision_types['top'] = True
                self.y_momentum=0
        return collision_types
    
    def shoot(self,W,H,mouseX,mouseY):
        #normalize the vector in the direction of the mouse
        dirx,diry=mouseX-self.rect.x,mouseY-self.rect.y
        norm=(dirx**2+diry**2)**(1/2)/10
        dirx,diry=dirx/norm,diry/norm
        return Net(W,H,self.rect.x,self.rect.y,dirx,diry,self.WIDTH,self.WIDTH,self.level)
        # return Net(self.WIDTH,self.WIDTH,self.rect.x,self.rect.y,10,0,self.WIDTH,self.WIDTH)