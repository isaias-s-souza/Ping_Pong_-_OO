import pygame

#Classe Sprite trás uma séries de recursos para tratar imagens
class Obj(pygame.sprite.Sprite):
    def __init__(self, img, *groups, right = -1, center = []):
        super().__init__(*groups)
        self.image = pygame.image.load(img)
        
        if right != -1:
            self.rect = self.image.get_rect(right = right)
        elif len(center) > 0:
            self.rect = self.image.get_rect(center = center)
        else:
            self.rect = self.image.get_rect()