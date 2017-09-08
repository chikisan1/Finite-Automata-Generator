import pygame
import random
from math import pi
import math


background_colour = (255,255,255)
(width, height) = (800, 600)


#colors
black = (0,0,0)
green = (200,0,0)
red = (0,255,0)

ivory = (238,233,233)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

pygame.display.flip()
clock = pygame.time.Clock()

circleCounter = 0

#position of the first circle
centerX = 200
centerY = 200

face = pygame.Surface((5, 5))

running = True
def circleButton(cx, cy):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    radius = cx + 40
    print(radius)
    px = mouse[0]
    py = mouse[1]
    print(px, py)
    pythag = math.sqrt(math.pow((px - cx), 2) + math.pow((py - cy), 2))
    print(pythag)
    if click[0] == 1 and ivory:
      pygame.draw.circle(screen, black, (cx, cy), 40)

def button(msg, x, y, w, h, ic, ac, action=None):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  global centerX
  global centerY
  global circleCounter
  if x+w > mouse[0] > x and y+h > mouse[1] > y:
    pygame.draw.rect(screen, ac,(x,y,w,h))
    if click[0] == 1 and action != None:
      if action == "Circle":
        if circleCounter == 0:
            pygame.draw.circle(screen, black, (centerX, centerY), 40, 2)
            circleCounter += 1
        else:
          centerX += 120
          pygame.draw.circle(screen, black, (centerX, centerY), 40, 2)
          circleCounter += 1
        print(circleCounter)
      elif action == "Line":
        if circleCounter != 0:
          pygame.draw.line(screen, (0,0,0), (300, 50), (300,100), 1)
  else:
    pygame.draw.rect(screen, ic,(x,y,w,h))

  smallText = pygame.font.Font("freesansbold.ttf", 20)
  textSurf, textRect = text_objects(msg, smallText)
  textRect.center = ((x+(w/2)), (y + (h/2)))
  screen.blit(textSurf, textRect)

def text_objects(text, font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect()

pygame.init()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  button("Circle", 150, 450, 100, 50, red, green, "Circle")
  button("Line", 550, 450, 100, 50, red, green, "Line")
  mouse = pygame.mouse.get_pos()
  circleButton(mouse[0], mouse[1])

  pygame.display.update()
  clock.tick(15)
