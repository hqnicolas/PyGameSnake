import pygame
from sys import exit
from game_logic import Game

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Cria instância do jogo
snake_game = Game(screen)

while True:
    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

 # Atualiza estado do jogo
    snake_game.update()

   # Desenha tudo
    screen.fill((0, 0, 0))
    snake_game.draw(screen)

   # Atualiza a exibição
    pygame.display.flip()

  # Limita taxa de quadros por segundo
    clock.tick(10)
