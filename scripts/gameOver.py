import pygame
from scripts.obj import Obj
from scripts.scene import Scene

class GameOver(Scene):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load("assets/gameOver.png")
        self.bg = Obj(self.img, [self.all_sprites])
