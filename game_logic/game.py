import pygame
from sys import exit
from snake_body import Snake, Food
from random import randint

class Game:
   def __init__(self, screen):
       self.screen = screen
       self.Snake = Snake()
       self.Food = Food()

   def update(self):
       # Processar entrada do teclado
       keys = pygame.key.get_pressed()

       if keys[pygame.K_UP] and not self.Snake.y == -10:
           self.Snake.y = -10
           self.Snake.x = 0

       if keys[pygame.K_DOWN] and not self.Snake.y == self.screen.get_height() - self.Snake.size:
           self.Snake.y = 10
           self.Snake.x = 0

       if keys[pygame.K_LEFT] and not self.Snake.x == -10:
           self.Snake.x = -10
           self.Snake.y = 0

       if keys[pygame.K_RIGHT] and not self.Snake.x == self.screen.get_width() - self.Snake.size:
           self.Snake.x = 10
           self.Snake.y = 0

       # Mover o cobra
       self.Snake.move()

   def draw(self, screen):
       # Desenhar a cobra e seu corpo
       for segment in self.Snake.body:
           pygame.draw.rect(screen, (0, 255, 0), (segment.x, segment.y, self.Snake.size, self.Snake.size))
           print(segment.x)
           print(segment.y)   
           # Verificar colisão 
           if (segment.x < -10 or segment.x >= self.screen.get_width() - self.Snake.size or segment.y < -10 or segment.y >= self.screen.get_height() - self.Snake.size):
              exit()
           # Verificar colisão com Alimento
           if self.Food.x-20 <= segment.x <= self.Food.x+20 and self.Food.y-20 <= segment.y <= self.Food.y+20:
              self.Food.bate()  # Respawn da comida em um novo local
              self.Snake.grow()
           print("food{}".format(self.Food.x))
           print("food{}".format(self.Food.y))


       # Desenhar o Alimento
       pygame.draw.rect(screen, (255, 0, 0), (self.Food.x, self.Food.y, self.Food.size, self.Food.size))

