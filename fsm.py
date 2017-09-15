import pygame
import random
import math

#CONSTANTS
BACKGROUND_COLOR = (255,255,255)
(WIDTH, HEIGHT) = (800, 600)

BLACK = (0,0,0)
GREEN = (200,0,0)
RED = (0,255,0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
circleCounter = 0

#position of the first circle
centerX = 200
centerY = 200

def circleButton(cx, cy):
    global screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    radius = cx + 40
    print(radius)

    px = mouse[0]
    py = mouse[1]
    print(px, py)

    pythag = math.sqrt(math.pow((px - cx), 2) + math.pow((py - cy), 2))
    print(pythag)

    if click[0] == 1:
      pygame.draw.circle(screen, BLACK, (cx, cy), 40)

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
            pygame.draw.circle(screen, BLACK, (centerX, centerY), 40, 2)
            circleCounter += 1
        else:
          centerX += 120
          pygame.draw.circle(screen, BLACK, (centerX, centerY), 40, 2)
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
  textSurface = font.render(text, True, BLACK)
  return textSurface, textSurface.get_rect()

def main():
    pygame.display.set_caption('Finite Automata Generator')
    screen.fill(BACKGROUND_COLOR)

    pygame.display.flip()
    clock = pygame.time.Clock()

    face = pygame.Surface((5, 5))

    running = True

    pygame.init()

    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      button("Circle", 150, 450, 100, 50, RED, GREEN, "Circle")
      button("Line", 550, 450, 100, 50, RED, GREEN, "Line")
      mouse = pygame.mouse.get_pos()
      circleButton(mouse[0], mouse[1])

      pygame.display.update()
      clock.tick(15)
      mouse = pygame.mouse.get_pos()

      if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, (200,0,0),(150,450,100,50))
            if pygame.mouse.get_pressed():
                    pygame.draw.circle(screen, (0, 0, 0), (300, 50), 40, 2)
      else:
            pygame.draw.rect(screen, (0,255,0),(150,450,100,50))
      
      pygame.display.update()
      clock.tick(15)

if __name__ == '__main__':
    main()
