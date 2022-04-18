from numpy import true_divide
import pygame
import random
 
class Ball(pygame.sprite.Sprite):
  #derives from the "Sprite" class in Pygame.
    
  def __init__(self, color, width, height):
    # Call the parent class (Sprite) constructor
    super().__init__()
    self.image = pygame.Surface([width, height])
    pygame.draw.rect(self.image,color, [0, 0, width, height])
    self.rect = self.image.get_rect()
    self.velocity = [2, -2]

  def setxy(self, x, y):
    self.rect.x=x
    self.rect.y=y
  
  def move(self):
    if self.rect.x < 10 and self.velocity[0] > 0:
      self.velocity[0] = -2
    elif  self.rect.x > 760 and self.velocity[0] < 0:
      self.velocity[0] = 2

    if self.rect.y < 50 and self.velocity[1] > 0:
      self.velocity[1] = -2
    elif self.rect.y > 580 and self.velocity[1] < 0:
      self.velocity[1] = 2
    
    self.rect.x -= self.velocity[0]
    self.rect.y -= self.velocity[1]
  
  def collide(self):
    self.velocity[1] *= -1
  
  def hitBottom(self):
    
    if self.rect.y > 580:
      self.velocity = [2, -2]
      return True
    return False