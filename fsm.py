import pygame
import random


background_colour = (255,255,255)
(width, height) = (800, 600)
 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

pygame.display.flip()
clock = pygame.time.Clock()


face = pygame.Surface((5, 5))

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  mouse = pygame.mouse.get_pos()


  if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
	pygame.draw.rect(screen, (200,0,0),(150,450,100,50))
	if pygame.mouse.get_pressed():
		pygame.draw.circle(screen, (0, 0, 0), (300, 50), 40, 2)
  else:
  	pygame.draw.rect(screen, (0,255,0),(150,450,100,50))
  
  pygame.display.update()
  clock.tick(15)