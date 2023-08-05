import pygame
import math
from Net import *
class Crow():
    def __init__(self, x_start, y_start, x_crop, y_crop, x_end, y_end):
        self.x_start,self.y_start = x_start,y_start
        self.x_crop,self.y_crop = x_crop,y_crop
        self.x_end,self.y_end = x_end,y_end
        self.x, self.y = x_start, y_start

        self.direction1 = 1
        if self.x_crop >= self.x: 
            self.direction1 = 1
        else:
            self.direction1 = -1

        self.direction2 = 1 
        if self.x_crop >= self.x_end: self.direction2 = -1
        else: self.direction2 = 1

        # slope 1 and 2 will be decided after phase 0 and phase 2 respectively
        self.slope1 = 0
        self.slope2 = 0

        self.velocity = 1
        self.rest_timer = 0
        self.see_Distance = 100
        self.current_frame = 0

        self.phase = 0

        #loading the images
        image_filenames = ['crow1_new.png', 'crow2_new.png', 'crow3_new.png', 'crow4_new.png', 'crow5_new.png', 'crow6_new.png', 'crow7_new.png']
        self.images = [pygame.image.load("./assets/images/crow/new/" + filename) for filename in image_filenames]
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (16 * 5, 16 * 5))

        self.set_images()


    def draw(self, win):
        self.move()
        if self.phase==2:
            self.current_frame = 5

        crow_rect = self.images[int(self.current_frame)].get_rect(topleft = (self.x, self.y))
        win.blit(self.images[int(self.current_frame)], crow_rect)
        self.current_frame += 0.5
        if self.current_frame == 7:
            self.current_frame = 0


    def move(self):
        if self.phase == 0:
            if abs(self.x_crop - self.x) < self.see_Distance:
                self.phase = 1
                self.slope1 = (self.y_crop - self.y) / (self.x_crop - self.x)
                self.set_images()
            else:
                self.x += self.direction1 * self.velocity
            
        elif self.phase == 1:
            if abs(self.x_crop - self.x) < 2 and abs(self.y_crop - self.y) < 2:
                self.phase = 2
                self.set_images()
            else:
                self.x += self.direction1 * self.velocity
                self.y += self.slope1 * self.direction1 * self.velocity

        elif self.phase == 2:
            if self.rest_timer >= 120:
                self.phase = 3
                self.slope2 = (self.y_end - self.y) / (self.x_end - self.x)
                self.set_images()
            else:
                self.rest_timer += 1
        
        else:
            if abs(self.y_end - self.y) < 2:
                self.y = self.y
            else:
                self.y += self.slope2 * self.direction2 * self.velocity
            self.x += self.direction2 * self.velocity

    def set_images(self):
        if self.phase == 0:
            if self.direction1 == 1:
                for i in range(len(self.images)):
                    self.images[i] = pygame.transform.flip(self.images[i], True, False)
        
        elif self.phase == 1:
            angle = math.degrees(math.atan(self.slope1)) + 180
            for i in range(len(self.images)):
                    self.images[i] = pygame.transform.rotate(self.images[i], angle)

        elif self.phase == 2:
            angle = math.degrees(math.atan(self.slope1)) + 180
            for i in range(len(self.images)):
                    self.images[i] = pygame.transform.rotate(self.images[i], -1 * angle)
        
        else:
            if self.direction2 != self.direction1:
               for i in range(len(self.images)):
                    self.images[i] = pygame.transform.flip(self.images[i], True, False)      