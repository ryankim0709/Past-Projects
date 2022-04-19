sky_blue = (142, 202, 230)
turqoise = (33, 158, 188)
navy = (2, 48, 71)
yellow = (255, 183, 3)
orange = (251, 133, 0)

from numpy import block
import pygame
from pyparsing import col
import paddle
import ball
import brick
import time
import tkinter as tk

#RGB colors for pygame elements; google color picker
WHITE = (255,255,255)
BLUE = (9,66,245)
BLACK = (0,0,0)
#globals
score = 0
lives = 3


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breakout Game")

#set groups
all_sprites_list = pygame.sprite.Group()
all_bricks = pygame.sprite.Group()


for i in range(7):
    block = brick.Brick(sky_blue, 80,30)
    block.setxy(i * 100 + 60, 100)
    all_bricks.add(block)
for i in range(7):
    block = brick.Brick(yellow, 80,30)
    block.setxy(i * 100 + 60, 150)
    all_bricks.add(block)
for i in range(7):
    block = brick.Brick(orange, 80,30)
    block.setxy(i * 100 + 60, 200)
    all_bricks.add(block)

paddle = paddle.Paddle(WHITE, 100, 10)
paddle.setxy(350,560)
all_sprites_list.add(paddle)

ball = ball.Ball(WHITE, 20, 20)
ball.setxy(386, 250)
all_sprites_list.add(ball)

playing = True

clock = pygame.time.Clock()
while playing:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False

  all_sprites_list.update()
  screen.fill(BLACK)
  pygame.draw.line(screen, WHITE, [0,38],[800,38],2)
  
  pScore = pygame.font.Font(None, 34).render("Score: " + str(score), 1, WHITE)
  pLives = pygame.font.Font(None, 34).render("Lives: " + str(lives), 1, WHITE)
  screen.blit(pScore, (20,10))
  screen.blit(pLives, (700, 10))
  all_sprites_list.draw(screen)
  all_bricks.draw(screen)
  pygame.display.flip()

  keys = pygame.key.get_pressed()
  if(keys[pygame.K_LEFT]):
    paddle.left()
  elif(keys[pygame.K_RIGHT]):
    paddle.right()
  ball.move()

  if pygame.sprite.collide_mask(ball, paddle):
    ball.collide()
  
  elif ball.hitBottom():
    lives -= 1
    ball.setxy(386, 250)
    all_sprites_list.draw(screen)
    time.sleep(2)
  
  brick_collisions = pygame.sprite.spritecollide(ball, all_bricks, False)
  for brick in brick_collisions:
    ball.collide()
    score += 1
    brick.kill()

  if score == 21:
    print("Congrats! You won!")
    playing = False
  if lives == 0:
    print("Sorry! You lost!")
    playing = False
  clock.tick(60)
 


pygame.quit()