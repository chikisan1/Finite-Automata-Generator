import pygame
import random
import math

circleCounter = 0
centerX = 200
centerY = 200

class Color:
  BACKGROUND_COLOR = (255,255,255)

  BLACK = (0,0,0)
  GREEN = (200,0,0)
  RED = (0,255,0)

class Draw:
  @staticmethod
  def button(screen, msg, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global centerX
    global centerY
    global circleCounter
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
      pygame.draw.rect(screen, active_color,(x,y,width,height))
      if click[0] == 1 and action != None:
        if action == "Circle":
          if circleCounter == 0:
              pygame.draw.circle(screen, Color.BLACK, (centerX, centerY), 40, 2)
              circleCounter += 1
          else:
            centerX += 120
            pygame.draw.circle(screen, Color.BLACK, (centerX, centerY), 40, 2)
            circleCounter += 1
          print(circleCounter)
        elif action == "Line":
          if circleCounter != 0:
            pygame.draw.line(screen, (0,0,0), (300, 50), (300,100), 1)
    else:
      pygame.draw.rect(screen, inactive_color,(x,y,width,height))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = Draw.text_objects(msg, smallText)
    textRect.center = ((x+(width/2)), (y + (height/2)))
    screen.blit(textSurf, textRect)

  @staticmethod
  def text_objects(text, font):
    textSurface = font.render(text, True, Color.BLACK)
    return textSurface, textSurface.get_rect()

class App:
  def __init__(self, width=800, height=800):
    self.screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Finite Automata Generator')
    pygame.display.flip()
    self.screen.fill(Color.BACKGROUND_COLOR)

    self.clock = pygame.time.Clock()
    self.running = False;

  def circleButton(self, cx, cy):
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
      pygame.draw.circle(self.screen, Color.BLACK, (cx, cy), 40)

  def start(self):
    self.running = True;
    
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      Draw.button(self.screen, "Circle", 150, 450, 100, 50, Color.RED, Color.GREEN, "Circle")
      Draw.button(self.screen, "Line", 550, 450, 100, 50, Color.RED, Color.GREEN, "Line")
      mouse = pygame.mouse.get_pos()
      self.circleButton(mouse[0], mouse[1])

      pygame.display.update()
      self.clock.tick(15)
      mouse = pygame.mouse.get_pos()

      if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
        pygame.draw.rect(self.screen, (200,0,0),(150,450,100,50))
        if pygame.mouse.get_pressed():
          pygame.draw.circle(self.screen, (0, 0, 0), (300, 50), 40, 2)
      else:
        pygame.draw.rect(self.screen, (0,255,0),(150,450,100,50))
      
      pygame.display.update()
      self.clock.tick(15)

def main(width, height):
  pygame.init()

  app = App()
  app.start()

if __name__ == '__main__':

    main(800, 600)
