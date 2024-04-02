import random

class Food:
    def __init__(self):
        x = ((10)*(random.randint(0, 64 - 1)))   # Gera uma posição aleatória para a comida no eixo x (entre 0 e 480 - 10)
        y = ((10)*(random.randint(0, 48 - 1)))  # Gera uma posição aleatória para a comida no eixo y (entre 0 e 640 - 10)
        self.x = x
        self.y = y
        self.size = 10

    def bate(self):
        x = ((10)*(random.randint(0, 64 - 1)))   # Gera uma posição aleatória para a comida no eixo x (entre 0 e 480 - 10)
        y = ((10)*(random.randint(0, 48 - 1)))  # Gera uma posição aleatória para a comida no eixo y (entre 0 e 640 - 10)
        self.x = x
        self.y = y
        self.size = 10
