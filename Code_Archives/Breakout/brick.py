import pygame

 
class Brick(pygame.sprite.Sprite):
  #derives from the "Sprite" class in Pygame.
    
  def __init__(self, color, width, height):
    # Call the parent class (Sprite) constructor
    super().__init__()
    
    self.image = pygame.Surface([width, height])
    pygame.draw.rect(self.image,color, [0, 0, width, height])
        
    # Fetch the rectangle object that has the dimensions of the image.
    self.rect = self.image.get_rect()

  def setxy(self, x, y):
    self.rect.x=x
    self.rect.y=y