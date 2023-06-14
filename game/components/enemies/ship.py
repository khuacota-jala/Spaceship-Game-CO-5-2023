import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1,ENEMY_2

class Ship(Enemy):
    WIDHT = 40
    HEIGHT = 60
    

    def __init__(self):
        self.image = [ENEMY_1, ENEMY_2]
        self.image = random.choice(self.image)
        self.image = pygame.transform.scale(self.image,(self.WIDHT,self.HEIGHT))
        super().__init__(self.image)